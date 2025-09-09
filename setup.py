import os
from setuptools import find_packages, setup


def fetch_requirements(path):
    with open(path, "r") as fd:
        return [r.strip() for r in fd.readlines()]


def fetch_readme():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


# Fetch readme
readme = fetch_readme()

setup(
    name="llama",
    version="0.0.1",
    packages=find_packages(
        include=["llama*"],
        exclude=("tests*", "examples*", "src*", "docs*", "benchmarks*"),
    ),
    description="Inference code for Llama models",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="Apache",
    url="https://github.com/meta-llama/llama",
    author="Meta AI Research",
    author_email="llama@meta.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="llm, large language model, machine learning, ai",
    install_requires=fetch_requirements("requirements.txt"),
    extras_require={
        "test": fetch_requirements("requirements-test.txt"),
        "dev": fetch_requirements("requirements-dev.txt"),
    },
    include_package_data=True,
    zip_safe=False,
)