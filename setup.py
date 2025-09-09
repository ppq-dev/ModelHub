import os
from setuptools import find_packages, setup


def fetch_requirements(path):
    with open(path, "r") as fd:
        return [r.strip() for r in fd.readlines()]


def fetch_readme():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


def fetch_version():
    with open("version.txt", "r") as f:
        return f.read().strip()


# Fetch readme
readme = fetch_readme()

# Fetch version
version = fetch_version()

setup(
    name="accelerate",
    version=version,
    packages=find_packages(
        include=["accelerate*"],
        exclude=("tests*", "examples*", "src*", "docs*", "benchmarks*"),
    ),
    description="A simple way to launch, train, and use PyTorch models on almost any device and distributed configuration, automatic mixed precision (including fp8), and easy-to-configure FSDP and DeepSpeed support",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="Apache",
    url="https://github.com/huggingface/accelerate",
    author="The HuggingFace team",
    author_email="accelerate@huggingface.co",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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
    keywords="pytorch, deep learning, machine learning, gpu, distributed, training",
    install_requires=fetch_requirements("requirements.txt"),
    extras_require={
        "test": fetch_requirements("requirements-test.txt"),
        "quality": fetch_requirements("requirements-quality.txt"),
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "accelerate=accelerate.commands.accelerate_cli:main",
        ]
    },
)