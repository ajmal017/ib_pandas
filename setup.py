"""Package description"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ib_pandas",
    version="0.1.0",
    author="Felix Baron",
    author_email="45421716+felixbaron@users.noreply.github.com",
    description="Interact with IB through pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/felixbaron/ib_pandas",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
