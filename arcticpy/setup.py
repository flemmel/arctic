"""
    Setup for ArCTIC cython wrapper. See README.md.

    Build with:
        python3 setup.py build_ext --inplace
"""

import os
import numpy as np
from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Build import cythonize

# Directories
dir_wrapper = os.path.dirname(os.path.realpath(__file__)) + "/"
dir_arctic = os.path.abspath(os.path.join(dir_wrapper, os.pardir)) + "/"
dir_include = dir_arctic + "include/"
dir_lib = dir_arctic
dir_gsl = dir_arctic + "gsl/"
dir_include_gsl = dir_gsl + "include/"
dir_lib_gsl = dir_gsl + "lib/"

# Clean
for root, dirs, files in os.walk(dir_wrapper, topdown=False):
    for name in files:
        file = os.path.join(root, name)
        if name.endswith(".o") or (
            name.startswith("wrapper")
            and not (name.endswith(".pyx") or name.endswith(".pxd"))
        ):
            print("rm", file)
            os.remove(file)

with open("README.md", "r") as f:
    long_description = f.read()

# Build
os.environ["CC"] = "g++"
setup(
    name="arcticpy",
    version="2.0",
    description="AlgoRithm for Charge Transfer Inefficiency Correction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jacob Kegerreis, Richard Massey, James Nightingale",
    author_email="jacob.kegerreis@durham.ac.uk",
    url="https://github.com/jkeger/arctic",
    license="GNU GPLv3+",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
    python_requires=">=3",
    keywords=["charge transfer inefficiency correction"],
    install_requires=["numpy"],
    packages=find_packages(),
    package_data={
        "": ["libarctic.so"]
    },
    ext_modules=cythonize(
        [
            Extension(
                "arcticpy.wrapper",
                sources=["arcticpy/wrapper.pyx", "arcticpy/interface.cpp"],
                language="c++",
                libraries=["arctic"],
                # library_dirs=[dir_lib, dir_lib_gsl],
                # runtime_library_dirs=[dir_lib, dir_lib_gsl],
                library_dirs=['arcticpy', dir_lib_gsl],
                runtime_library_dirs=['arcticpy', dir_lib_gsl],
                include_dirs=[dir_include, np.get_include(), dir_include_gsl],
                extra_compile_args=["-std=c++11", "-O3"],
                # extra_link_args=['-install_name', "arcticpy/libarctic.so"],
                define_macros=[('NPY_NO_DEPRECATED_API', 0)],
            )
        ],
        compiler_directives={"language_level": "3"},
    )
)
