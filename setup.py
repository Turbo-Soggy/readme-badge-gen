from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="readme-badge-gen",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A dead simple CLI tool to generate README badges",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/readme-badge-gen",
    py_modules=["badge_gen"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "badge-gen=badge_gen:main",
        ],
    },
)
