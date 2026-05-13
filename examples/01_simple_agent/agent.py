"""
Track 01 Agent - Smart task execution workflow.

This module provides a practical single-agent implementation that can:
- prioritize a task backlog,
- allocate day plans with time blocks,
- identify execution risks,
- propose concrete next actions.
"""

from typing import Any, Dict, List, Tuple
from pathlib import Path
from datetime import datetime
import json
import re
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools import tool
import logging

logger = logging.getLogger(__name__)


URGENT_KEYWORDS = {"urgent", "asap", "today", "deadline", "critical", "blocker"}
IMPACT_KEYWORDS = {"client", "production", "release", "interview", "proposal", "paper"}
LOW_EFFORT_KEYWORDS = {"email", "review", "fix", "check", "draft", "update"}


def _extract_tasks(raw: str) -> List[str]:
    lines = [line.strip("- ").strip() for line in raw.splitlines() if line.strip()]
    if len(lines) <= 1 and "," in raw:
        lines = [part.strip() for part in raw.split(",") if part.strip()]
    return lines


def _extract_hours(text: str) -> float:
    match = re.search(r"(\d+(?:\.\d+)?)\s*h", text.lower())
    if match:
        return float(match.group(1))
    return 1.0


def _time_add(start_hour: int, start_minute: int, minutes_to_add: int) -> Tuple[int, int]:
    total = start_hour * 60 + start_minute + minutes_to_add
    return total // 60, total % 60


@tool
def prioritize_backlog(tasks: str) -> str:
    """Prioritize tasks from newline or comma-separated input. Add optional effort like '(2h)'."""
    parsed_tasks = _extract_tasks(tasks)
    if not parsed_tasks:
        return "No tasks found. Provide tasks as lines or comma-separated items."

    scored = []
    for task in parsed_tasks:
        lower = task.lower()
        hours = _extract_hours(task)
        urgency = sum(1 for keyword in URGENT_KEYWORDS if keyword in lower)
        impact = sum(1 for keyword in IMPACT_KEYWORDS if keyword in lower)
        quick_win = sum(1 for keyword in LOW_EFFORT_KEYWORDS if keyword in lower)

        score = 5 + (urgency * 2) + impact + quick_win - (0.4 * hours)
        reason = f"urgency={urgency}, impact={impact}, quick_win={quick_win}, effort={hours:.1f}h"
        scored.append((score, task, reason))

    scored.sort(key=lambda x: x[0], reverse=True)
    lines = ["Priority Order:"]
    for idx, item in enumerate(scored, 1):
        lines.append(f"{idx}. {item[1]}  [score={item[0]:.1f}; {item[2]}]")

    return "\n".join(lines)


@tool
def build_day_plan(plan_request: str) -> str:
    """Build a time-blocked daily plan from tasks. Include effort markers like '(2h)' when possible."""
    tasks = _extract_tasks(plan_request)
    if not tasks:
        return "No tasks found for planning."

    available_match = re.search(r"hours\s*[:=]\s*(\d+(?:\.\d+)?)", plan_request.lower())
    available_hours = float(available_match.group(1)) if available_match else 6.0
    available_minutes = int(available_hours * 60)

    current_h, current_m = 9, 0
    used = 0
    lines = [f"Daily Plan (available={available_hours:.1f}h):"]

    for task in tasks:
        effort_minutes = int(_extract_hours(task) * 60)
        if used + effort_minutes > available_minutes:
            lines.append(f"- Backlog: {task}")
            continue

        end_h, end_m = _time_add(current_h, current_m, effort_minutes)
        lines.append(
            f"- {current_h:02d}:{current_m:02d}-{end_h:02d}:{end_m:02d} | {task}"
        )

        used += effort_minutes
        current_h, current_m = _time_add(end_h, end_m, 10)

    remaining = max(0, available_minutes - used)
    lines.append(f"Remaining capacity: {remaining // 60}h {remaining % 60}m")
    return "\n".join(lines)


@tool
def assess_execution_risks(tasks: str) -> str:
    """Assess dependency and execution risks from a task list or plan."""
    parsed_tasks = _extract_tasks(tasks)
    if not parsed_tasks:
        return "No tasks found for risk assessment."

    risk_terms = {
        "waiting": "External dependency",
        "approval": "Stakeholder dependency",
        "blocked": "Execution blocker",
        "unknown": "Requirement ambiguity",
        "integrate": "Integration risk",
    }
    risks = []

    for task in parsed_tasks:
        lower = task.lower()
        for keyword, label in risk_terms.items():
            if keyword in lower:
                risks.append((task, label, keyword))

    if not risks:
        return "Risk Review:\n- No explicit high-risk dependency keywords detected. Add assumptions and owners for each task."

    lines = ["Risk Review:"]
    for idx, risk in enumerate(risks, 1):
        lines.append(f"{idx}. {risk[0]} -> {risk[1]} (trigger='{risk[2]}')")
    lines.append("Mitigation: assign owner, define due date, and specify unblock condition per risk.")
    return "\n".join(lines)


@tool
def suggest_next_actions(task: str) -> str:
    """Generate immediate next actions for a single task description."""
    t = task.strip()
    if not t:
        return "Provide one task description to generate next actions."

    lower = t.lower()
    if "interview" in lower:
        actions = [
            "Define target role scope and top 3 interview themes.",
            "Prepare 5 STAR stories mapped to role requirements.",
            "Run a 30-minute mock interview and capture gaps.",
        ]
    elif "proposal" in lower or "paper" in lower:
        actions = [
            "Draft a one-page outline with objective, method, and expected outcomes.",
            "List missing references and gather supporting material.",
            "Schedule a focused writing block and complete first draft section.",
        ]
    elif "release" in lower or "deploy" in lower:
        actions = [
            "Freeze scope and finalize release checklist.",
            "Run smoke tests on staging and record outcomes.",
            "Prepare rollback notes and communication update.",
        ]
    else:
        actions = [
            "Clarify deliverable and acceptance criteria.",
            "Break the task into 2-3 executable subtasks.",
            "Schedule the first focused work block on calendar.",
        ]

    lines = [f"Next Actions for: {t}"]
    for idx, action in enumerate(actions, 1):
        lines.append(f"{idx}. {action}")
    return "\n".join(lines)


@tool
def export_plan_json(plan_text: str, output_file: str = "logs/track01_execution_plan.json") -> str:
    """Export a plan or agent output to a JSON file path relative to the repository root."""
    if not plan_text.strip():
        return "No plan content provided to export."

    repo_root = Path(__file__).resolve().parents[2]
    target_path = (repo_root / output_file).resolve()

    # Prevent writing outside repository boundaries.
    if repo_root not in target_path.parents and target_path != repo_root:
        return "Invalid output path: file must be inside the repository."

    target_path.parent.mkdir(parents=True, exist_ok=True)

    items = [line.strip("- ").strip() for line in plan_text.splitlines() if line.strip()]
    payload = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "agent": "Track01SmartTaskExecution",
        "output_file": str(target_path.relative_to(repo_root)),
        "plan_text": plan_text,
        "items": items,
    }

    with target_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    return f"Plan exported to {target_path.relative_to(repo_root)}"


class SimpleAgent:
    """
    A simple agent that uses LangChain's built-in agent framework.
    
    Smart Task Execution Agent using LangChain's built-in agent framework.

    This agent is designed for practical planning workflows:
    - backlog prioritization,
    - day-plan generation,
    - risk assessment,
    - actionable next steps.
    """

    def __init__(self, verbose: bool = True):
        """
        Initialize the smart task execution agent.

        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        self.agent = None
        self.tools = self._setup_tools()
        self._initialize_agent()

    def _setup_tools(self) -> List[Tool]:
        """Set up available tools."""
        tools = [
            Tool(
                name="prioritize_backlog",
                func=prioritize_backlog.invoke,
                description="Prioritize task lists based on urgency, impact, and effort.",
            ),
            Tool(
                name="build_day_plan",
                func=build_day_plan.invoke,
                description="Create a time-blocked day plan from a list of tasks and available hours.",
            ),
            Tool(
                name="assess_execution_risks",
                func=assess_execution_risks.invoke,
                description="Identify dependency and execution risks in a plan or task list.",
            ),
            Tool(
                name="suggest_next_actions",
                func=suggest_next_actions.invoke,
                description="Generate concrete next actions for one task.",
            ),
            Tool(
                name="export_plan_json",
                func=export_plan_json.invoke,
                description="Save plan output as JSON into the repository, e.g. logs/track01_execution_plan.json.",
            ),
        ]
        return tools

    def _initialize_agent(self):
        """Initialize the LangChain agent."""
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=self.verbose,
            max_iterations=6,
            handle_parsing_errors=True,
        )

    def run(self, task: str) -> str:
        """
        Run the agent on a task.

        Args:
            task: The task description

        Returns:
            Agent's response
        """
        try:
            result = self.agent.invoke({"input": task})
            return result.get("output", "")
        except Exception as e:
            logger.error(f"Agent error: {e}")
            return f"Error executing task: {str(e)}"

    def execute(self, task: str) -> Dict[str, Any]:
        """
        Execute a task and return detailed results.

        Args:
            task: The task description

        Returns:
            Dictionary with execution details
        """
        try:
            result = self.agent.invoke({"input": task})
            return {
                "success": True,
                "output": result.get("output", ""),
                "task": task,
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "task": task,
            }

    def get_tools_info(self) -> List[Dict[str, str]]:
        """Get information about available tools."""
        return [
            {
                "name": tool.name,
                "description": tool.description,
            }
            for tool in self.tools
        ]
