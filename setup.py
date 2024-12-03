from setuptools import setup,find_packages

with open("readme.md","r",encoding="utf8") as f:
    descriptionL = f.read()

setup(
        name="Anticord",
        version="0.4",
        packages=find_packages(),
        long_description=descriptionL,
        description="Discord api wrapper",
        author="Spiderman from earth 69",
        author_email="spidermanfromearth69@gmail.com",
        install_requires=[
            'websocket',
            'requests',
        ],
        long_description_content_type = 'text/markdown'
)


