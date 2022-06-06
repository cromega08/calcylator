from setuptools import setup

setup(name = "calcylator",
    version = "1.0.0",
    entry_points = {
        "console_scripts" : ["calcylator=calcylator:run"]
    }
)