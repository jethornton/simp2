from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="simple_import",
    version="0.0.6",
    author="John Doe",
    author_email="<doe.john@example.com>",
    description="Hello - An example to test install and docs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jethornton/hello",
    download_url="https://github.com/jethornton/hello/tarball/master",
    python_requires='>=3',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': ['simple-import=simple_import.simple_import:main',],
    },
)

