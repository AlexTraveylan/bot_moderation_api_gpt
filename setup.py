from setuptools import setup, find_packages

setup(
    name="template-example",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "template-example = template-example.app:main",
        ]
    },
    author="Alex Traveylan",
    author_email="alex.traveylan@gmail.com",
    description="A bot for legend of solgard",
    url="https://github.com/AlexTraveylan/templateExample",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
