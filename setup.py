import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pokelastic",
    version="0.1.0",
    author="Thomas PERROT",
    author_email="thomas_perrot@ultimatesoftware.com",
    description="An introduction projet to Elasticsearch with Pokemon",
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)