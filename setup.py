from setuptools import setup, find_packages
import os

# Read requirements
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Read README file
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
long_description = ""
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="anime_recommender",
    version="0.1",
    author="Paras",
    description="An AI-powered anime recommendation system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["pipeline", "utils", "src", "config", "app"]),
    package_data={"": ["*.csv", "*.env"]},
    install_requires=requirements,
    python_requires=">=3.8",
)