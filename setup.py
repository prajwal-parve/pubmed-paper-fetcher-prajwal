from setuptools import setup, find_packages

setup(
    name="pubmed_paper_fetcher",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "pubmed-fetch=pubmed_paper_fetcher.main:main",
        ],
    },
    author="Your Name",
    description="A tool to fetch and filter research papers from PubMed",
    url="https://github.com/yourusername/pubmed_paper_fetcher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
