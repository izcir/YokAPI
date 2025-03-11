from setuptools import setup, find_packages

setup(
    name="YokAPI",
    version="1.1.0",
    author="IZCI",
    author_email="email@example.com",
    description="Unofficial  API for YokAtlas",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/izcir/YokAPI",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "aiohttp==3.11.13",
        "certifi==2025.1.31",
        "bs4==0.0.2",
        "pydantic==2.10.6"    
    ],
    license="MIT"
)
