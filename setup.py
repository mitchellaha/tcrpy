import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tcrpy",
    version="0.2.0",
    author="Mitch V Aureli",
    author_email="mitch@logic3ii.com",
    description="A Python Library for Interacting with the TCR Platform API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mitchellaha/tcrpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        'beautifulsoup4==4.11.1',
        'pydantic==1.9.0',
        'python-dotenv==0.20.0',
        'requests==2.27.1'
    ],
)