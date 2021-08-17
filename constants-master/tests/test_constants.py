#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring,no-member,no-name-in-module

import lisaconstants
from lisaconstants import c


def test_speed_of_light():
    """Test the value of `SPEED_OF_LIGHT`."""
    assert lisaconstants.SPEED_OF_LIGHT == 299792458

def test_c():
    """Test the value of the alias `c`."""
    assert c == 299792458
