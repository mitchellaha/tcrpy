import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TCRAPI",
    version="0.1.0",
    author="Mitch V Aureli",
    author_email="mitch@logic3ii.com",
    description="A Python Library For Interacting With TCR",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mitchellaha/TCR-API",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    install_requires=[
        'beautifulsoup4==4.11.1',
        'pydantic==1.9.0',
        'python-dotenv==0.20.0',
        'requests==2.27.1'
    ],
)