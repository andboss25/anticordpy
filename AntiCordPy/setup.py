from setuptools import setup,find_packages

with open("readme.md","r") as f:
    descriptionL = f.read()

setup(
        name="Anticord",
        version="0.1",
        packages=find_packages(),
        long_description=descriptionL,
        description="Discord api wrapper",
        author="Spiderman from earth 69",
        author_email="spidermanfromearth69@gmail.com",
        install_requires=[
            'websocket',
            'requests',
    ],
)

# TODO upload on pypi and on github , make sure not to leak password
