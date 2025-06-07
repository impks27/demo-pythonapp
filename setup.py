from setuptools import setup, find_packages

setup(
    name="demo_python_app",
    version="0.1.0",
    description="A simple example Python app",
    author="Your Name",
    author_email="your@email.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
