import sys

from setuptools_scm.utils import do


def test_parentdir_prefix(tmpdir):
    p = tmpdir.ensure("projectname-v2.1", dir=True)
    p.join("setup.py").write(
        """from setuptools import setup
setup(generate_conda_recipe=True)
"""
    )
    res = do((sys.executable, "setup.py", "--version"), p)
    print(res)
