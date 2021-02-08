import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="puzzle_ivddorrka",
    version="0.0.1",
    author="Daria Kuzmina",
    author_email="darya.kuzmina@ucu.edu.ua",
    description="Project checks whether the field is ready to play with",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ivddorrka/puzzle_lab1.2.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)
