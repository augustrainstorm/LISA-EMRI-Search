# LISA Constants

LISA Constants is a Python package providing values sanctioned by the LISA Consortium for physical constants and mission parameters. LISA Constants is intended to be consistently used by other pieces of software related to the simulation of the instrument, of gravitational wave signals, and others.

We provide support for Python projects (as a package), C projects (as a header file), and C++ projects (as a header file). See below how to use the package.

The list of available constants is available [here](https://gitlab.in2p3.fr/lisa-simulation/constants/-/blob/master/lisaconstants/constants.py).

## Usage

Install lisaconstants using pip,
```
pip install git+https://gitlab.in2p3.fr/lisa-simulation/constants.git
```

Install from source:
```
pip install .
```
or alternatively

```
python setup.py install install_headers
```

### Python

Simply import lisaconstants to access the constants,
```
from lisaconstants import c
light_minute = 60 * c
```

### C

Include lisaconstants.h (automatically placed in your current Python installation's include directory). Constants are prefixed with "LISA_" to prevent name collisions.
```
#include "venv/include/lisaconstants.h"
double lightMinute = 60 * LISA_c;
```

### C++

Include lisaconstants.hpp (automatically placed in your current Python installation's include directory). Constants are defined in the `LisaConstants` namespace to prevent name collisions.
```
#include "venv/include/lisaconstants.h"
double lightMinute = 60 * LisaConstants::c;
```

## Add LISA Constants to your project

### As a setup.py requirement

If your project is built as a Python package, we strongly recommend to add lisaconstants as a dependency in your setup.py file.
```
setup(
  name="mypackage",
  # ...
  install_requires=[
    "lisaconstants @ git+https://gitlab.in2p3.fr/lisa-simulation/constants.git"
  ],
)
```

### As a pip requirement

Install lisaconstants locally with pip, then add it to a requirement.txt, which can be checked in on your repository,
```
pip install git+https://gitlab.in2p3.fr/lisa-simulation/constants.git
pip freeze > requirements.txt
```

Users will be able to install your dependencies using
```
pip install -r requirements.txt
```

### Silence static linter warnings

LISA Constants dynamically generates the constants when the module is imported. Static linters (syntax analyzers), such as Pylint, do not import the module and therefore incorrectly issue warnings for each constant imported from LISA Constants. To silence these warnings, create a file ".pylintrc" if it does not exist, and add the following commands
```
[TYPECHECK]

ignored-modules=lisaconstants
```

## Contributing

### Report an issue

We use the issue-tracking management system associated with the project provided by Gitlab. If you want to report a bug or request a feature, open an issue at https://gitlab.in2p3.fr/lisa-simulation/constants/-/issues. You may also thumb-up or comment on existing issues.

### Development environment

We strongly recommend to use [Python virtual environments](https://docs.python.org/3/tutorial/venv.html).

To setup the development environment, use the following commands:
```
git clone git@gitlab.in2p3.fr:lisa-simulation/constants.git
cd python-constants
python -m venv .
source ./bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Workflow

The project's development workflow is based on the issue-tracking system provided by Gitlab, as well as peer-reviewed merge requests. This ensures high-quality standards.

Issues are solved by creating branches and opening merge requests. Only the assignee of the related issue and merge request can push commits on the branch. Once all the changes have been pushed, the "draft" specifier on the merge request is removed, and the merge request is assigned to a reviewer. He can push new changes to the branch, or request changes to the original author by re-assigning the merge request to them. When the merge request is accepted, the branch is merged onto master, deleted, and the associated issue is closed.

### Pylint and unittest

We enforce [PEP 8 (Style Guide for Python Code)](https://www.python.org/dev/peps/pep-0008/) with Pylint syntax checking, and correction of the code using the [pytest](https://docs.pytest.org/)] testing framework. Both are implemented in the continuous integration system.

You can run them locally
```
pylint **/*.py
python -m pytest
```

## Contact

* Jean-Baptiste Bayle (j2b.bayle@gmail.com)
* Maude Lejeune (lejeune@apc.in2p3.fr)
* Aurelien Hees (aurelien.hees@obspm.fr)
