# Tutorial
## Initialization
Reference :
* Basic : https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/
* Basic : https://towardsdatascience.com/requirements-vs-setuptools-python-ae3ee66e28af
* Advance : https://towardsdatascience.com/setuptools-python-571e7d5500f2
* Advance : https://www.jianshu.com/p/47a4979ef318

## setup.py
setuptools is a package built on top of distutils that allows developers to develop and distribute Python packages. It also offers functionality that makes dependency management easier.

When you want to release a package, you normally need some metadata including the package name, version, dependencies, entry points, etc. and setuptools offers the functionality to do exactly this.

The project metadata and options are defined in a setup.py file, as shown below.
```python
from setuptools import setup
setup(     
    name='mypackage',
    author='Giorgos Myrianthous',     
    version='0.1',     
    install_requires=[         
        'pandas',         
        'numpy',
        'matplotlib',
    ],
    # ... more options/metadata
)
```
In fact, this is considered to be a somewhat bad design given that the file is purely declarative. Therefore, a better approach is to define these options and metadata in a file called setup.cfg and then simply call setup() in your setup.py file. An example setup.cfg file is illustrated below:
```conf
[metadata]
name = mypackage
author = Giorgos Myrianthous
version = 0.1[options]
install_requires =
    pandas
    numpy
    matplotlib
```
and finally, you can have a minimal setup.py file:
```python
from setuptools import setup
if __name__ == "__main__":
    setup()
```
Note that the install_requires argument can take a list of dependencies along with their specifiers (including the operators <, >, <=, >=, == or !=, followed by a version identifier. Therefore, when the project gets installed, every dependency that isn’t already satisfied in the environment will be located on PyPI (by default), downloaded and installed.

## requirements.txt
The requirements.txt is a file listing all the dependencies for a specific Python project. It may also contain dependencies of dependencies, as discussed previously. The listed entries can be pinned or non-pinned. If a pin is used, then you can specify a specific package version (using ==), an upper or lower bound or even both.
Example
```bash
matplotlib>=2.2
numpy>=1.15.0, <1.21.0
pandas
pytest==4.0.1
```
Finally, you could install these dependencies (normally in a virtual environment) through pip using the following command:
```bash
pip install -r requirements.txt
```
In the example requirements file above, we specified a few dependencies using various pins. For example, for the pandas package that has no pin associated to it, pip will normally install the latest version, unless one of the other dependencies has any conflict with this (in this case pip will normally install the latest pandas version that satisfies the conditions specified by the remaining dependencies). Now going forward, for pytest the package manager will install the specific version (i.e. 4.0.1) while for matplotlib, will install the latest version, which is at least greater or equal than 2.2 (again this depends on whether another dependency specifies otherwise). Finally, for numpy package, pip will attempt to install the latest version between versions 1.15.0 (inclusive) and 1.21.0 (non-inclusive).

Once you install all the dependencies, you can see the precise version of each dependency installed in the virtual environment by running pip freeze. This command will list all the packages along with their specific pins (i.e. ==).

The requirements file is extremely useful but in most of the cases, it must be used for development purposes. If you are planning to distribute your package so that it is widely available (say on PyPI), you may need something more than just this file.