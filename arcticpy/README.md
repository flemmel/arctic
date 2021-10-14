# ArCTIC Python wrapper

## Installation

* Build GSL libraries: `make gsl`
* Build Arctic library: `make lib`
* Build ArcticPy library and wheel file:
```bash
$ cd arcticpy
$ python setup.py build_ext --inplace
$ python setup.py bdist_wheel
```
* Install ArcticPy wrapper:
```bash
$ pip install dist/arcticpy-2.0-cp39-cp39-macosx_10_15_x86_64.whl
```