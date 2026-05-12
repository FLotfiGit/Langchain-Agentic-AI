from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="langchain-agentic-ai",
    version="0.1.0",
    author="Fatemeh Lotfi",
    author_email="flotfi@clemson.edu",
    description="LangChain agentic AI project by Fatemeh Lotfi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FLotfiGit/Langchain-Agentic-AI",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    install_requires=[
        "langchain>=0.1.0",
        "langchain-openai>=0.0.1",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
    ],
)
