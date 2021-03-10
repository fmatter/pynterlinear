import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pynterlinear",
    version="0.0.1",
    author="Florian Matter",
    author_email="florianmatter@gmail.com",
    description="Converts interlinear text from any source to LaTeX and Microsoft Word",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="-",
    packages=setuptools.find_packages(),
    install_requires=[
        "python-docx",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)