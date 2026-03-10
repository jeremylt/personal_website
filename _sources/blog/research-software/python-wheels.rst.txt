Python Wheel Versions
********************************************************************************

I found a curious and frustrating issue with an outdated version of a dependency being installed in my `venv`.


Issue
================================================================================

The package `rapidyaml <https://github.com/biojppm/rapidyaml>`_ is required for `4C <https://github.com/4C-multiphysics/4C>`_.
During install of dependencies for the development environment, `rapidyaml-0.1.0.post60-cp314-cp314-linux_x86_64.whl` was installed instead of the newer `rapidyaml-0.10.0*`.
When attempting to install the package manually on my system, the latest version was indeed used instead of the outdated version.


Diagnosis
================================================================================

I am not as familiar with Python dependency management as I would like to be.
The command `pip install foo -vv` (or `-vvv`) prompts `pip` to be more verbose.
The verbose output indicated that `pip` was searching `https://pypi.org/simple/rapidyaml <https://pypi.org/simple/rapidyaml>`_ for compatible packages.

The `pypi simple repository API <https://packaging.python.org/en/latest/specifications/simple-repository-api>`_ lists only the download links for a specific Python package.
For instance, the package `foo` has its download links listed at `https://pypi.org/simple/foo`.

Although this package had enabled `wheels for Python 3.14 <https://github.com/biojppm/rapidyaml/pull/571>`_, these wheels were not listed on `rapidyaml's simple repository API page <https://pypi.org/simple/rapidyaml>`_.
Oddly enough, there was a wheel with support for Python 3.14, but only for v0.1.0 of `rapidyaml` and no other version.


Fix
================================================================================

The only fixes I've identified are

* Ask the package maintainer to fix the listed wheels

* Use a supported version of Python

* Manually install the package from source


Metadata
================================================================================

Started: 11 Mar 2026
Last edited: 11 Mar 2026
