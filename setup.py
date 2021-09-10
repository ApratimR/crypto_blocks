import setuptools


def readme():
    with open("readme.md") as f:
        return f.read()


setuptools.setup(
    name="cryptoblocks64",
    version="0.0.4",
    author="Apratim Ray",
    author_email="apratimr55@gmail.com",
    description="A collection of common cryptography related functions but in B64 operation format",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ApratimR/crypto_blocks",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="cryptoblocks64"),
    py_modules=["cryptoblocks64"],
    install_requires=["numpy"],
    python_requires=">=3.6",
)
