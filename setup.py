import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ballon",
    version="0.0.1",
    author="hglf",
    author_email="hgleifeng@foxmail.com",
    description="A small package help bypassing scrolling captchas",
    long_description_content_type="text/markdown",
    url="https://github.com/hotstu/ballon",
    project_urls={
        "Bug Tracker": "https://github.com/hotstu/ballon/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)