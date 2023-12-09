from pathlib import Path

from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

analysis_packes = ["jupyterlab==3.4.6"]
docs_packages = ["mkdocs==1.3.0", "mkdocstrings==0.18.1"]
# Define our package
setup(
    name="Car Price Prediction",
    version=1.0,
    description="ervice that takes information about a car and return the predicted price for that car.",
    author="Lojain Azzam",
    author_email="logainazzam@gmail.com",
    python_requires=">=3.7",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
    extras_require={
        "dev": analysis_packes,
        "docs": docs_packages,
    },
)