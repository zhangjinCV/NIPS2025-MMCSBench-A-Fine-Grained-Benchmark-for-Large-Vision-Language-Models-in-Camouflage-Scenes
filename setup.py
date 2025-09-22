from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="mmcsbench",
    version="1.0.0",
    author="Jin Zhang",
    author_email="",
    description="A Fine-Grained Benchmark for Large Vision-Language Models in Camouflage Scenes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhangjinCV/NIPS2025-MMCSBench-A-Fine-Grained-Benchmark-for-Large-Vision-Language-Models-in-Camouflage-Scenes",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "isort>=5.10.0",
            "pre-commit>=2.15.0",
        ],
        "docs": [
            "sphinx>=4.3.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="computer vision, natural language processing, benchmark, camouflage, vision-language models",
)