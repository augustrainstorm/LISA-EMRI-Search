#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring,no-member,no-name-in-module

import os

from lisaconstants.constants import Constant
from lisaconstants.cheader import HeaderGenerator


Constant('LIFE_UNIVERSE', 42, None, 'Answer to life, the Universe and everything')
Constant('TEAPOT', '418', None, 'I am a teapot')
Constant.alias('l', 'LIFE_UNIVERSE')


def word_in_file(word, filename):
    """Check that a word can be found in file.

    Args:
        word: word to find
        file: path to file
    """
    with open(filename, 'r') as file:
        for line in file.readlines():
            if word in line:
                return True
    return False


def test_cpp():
    """Test generation of C++ header."""
    filename = 'lisaconstants.hpp'
    HeaderGenerator(Constant.ALL).write(filename, 'c++')
    assert os.path.exists(filename)
    assert word_in_file('LIFE_UNIVERSE', filename)
    assert word_in_file('TEAPOT', filename)
    assert word_in_file('l', filename)


def test_c():
    """Test generation of C header."""
    filename = "lisaconstants.h"
    HeaderGenerator(Constant.ALL).write(filename, 'c')
    assert os.path.exists(filename)
    assert word_in_file('LISA_LIFE_UNIVERSE', filename)
    assert word_in_file('LISA_TEAPOT', filename)
