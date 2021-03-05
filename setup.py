import setuptools

if __name__ == "__main__":
    setuptools.setup(
        author="Karl Erik Levik, Markus Gerstel",
        author_email="scientificsoftware@diamond.ac.uk",
        scripts=["bin/dimple2ispyb.py", "bin/mxdatareduction2ispyb.py"],
        tests_require=["pytest"],
    )
