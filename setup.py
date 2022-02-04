# https://packaging.python.org/en/latest/tutorials/packaging-projects/
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latestEarthquakeID",
    version="0.0.1",
    author="TheoBrata",
    author_email="theodoresibp@gmail.com",
    description="This package will get the latest earthquake in Indonesia from BMKG | Meteorological, Climatological, "
                "and Geophysical Agency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)