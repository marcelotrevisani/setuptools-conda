import setuptools


def generate_conda_recipe(dist: setuptools.Distribution, keyword, value):
    if not value:
        return
    breakpoint()
    print(dist)
