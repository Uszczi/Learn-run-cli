from setuptools import setup

setup(
    name="learn-run-cli",
    version="1.0",
    packages=["lrc"],
    entry_points={
        "console_scripts": [
            "learn-run-cli = lrc.main:main"
        ]
    },
)
