#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""LISA Python Constant module."""

import sys

from .meta import __version__
from .meta import __author__
from .meta import __email__

from .constants import Constant

# Iterate over constants and set their values as
# attributes of the current module for easy access
for name, constant in Constant.ALL.items():
    vars()[name] = constant.value
