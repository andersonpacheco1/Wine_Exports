from setuptools import find_packages, setup

setup(
    name="wine-project",
    version="0.1.0",
    description="Wine dashboard project with Streamlit",
    author="S. Costa",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dashboard = app.__main__:main"
        ]
    }
)
