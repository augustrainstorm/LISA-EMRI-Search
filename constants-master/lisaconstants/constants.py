#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LISA Python Constants.

This module provides values sanctioned by the LISA Consortium for physical constants and mission parameters.

LISA Python Constants is intended to be consistently used by other pieces of software related to the simulation of
the instrument, of gravitational wave signals, and others.

Authors:
    Jean-Baptiste Bayle <j2b.bayle@gmail.com>
    Aurelien Hees <aurelien.hees@obspm.fr>
    Maude Lejeune <lejeune@apc.in2p3.fr>
"""

class Constant:
    """Defines a constant with associated metadata.

    Attributes:
        ALL: dictionary of all constants
    """

    ALL = {}

    @classmethod
    def alias(cls, name, original):
        """Give an existing constant an alias name.

        Args:
            name: alias name
            original: original name
        """
        cls.ALL[name] = cls.ALL[original]

    def __init__(self, name, value, unit, description, error=None, references=None):
        """Initialize a constant with attributes.

        Args:
            name: constant name
            value: constant value
            unit: associated unit, or None
            description: description
            error: uncertainty on value, or None
            references: list of references, or None
        """
        self.name = str(name)
        self.value = value
        self.description = str(description)
        self.unit = unit
        self.error = error

        if references is None:
            self.references = []
        elif isinstance(references, str):
            self.references = [references]
        else:
            self.references = references

        # Add to list of defined constants
        self.ALL[name] = self

    def __repr__(self):
        if self.unit is None:
            return f'<{self.name} ({self.value})>'
        return f'<{self.name} ({self.value} {self.unit})'


Constant('SPEED_OF_LIGHT', 299792458.0, 'm/s',
    "Speed of light in a vacuum",
    ["P.J. Mohr, B.N. Taylor, D.B. Newell, 9 July 2015, 'The 2014 CODATA Recommended Values of the Fundamental"
    "Physical Constants', National Institute of Standards and Technology, Gaithersburg, MD 20899-8401;"
    "http://www.codata.org/",
    "http://physics.nist.gov/constants (Web Version 7.0). See also the IAU (2009) System of Astronomical Constants"
    "(IAU, August 2009, 'IAU 2009 Astronomical Constants', IAU 2009 Resolution B2 adopted at the XXVII-th General"
    "Assembly of the IAU. See also IAU, 10 August 2009, 'IAU WG on NSFA Current Best Estimates',"
    "http://maia.usno.navy.mil/NSFA/NSFA_cbe.html)"])

Constant.alias('c', 'SPEED_OF_LIGHT')

Constant('SIDEREALYEAR_J2000DAY', 365.256363004, 'day',
    "Number of days per sidereal year",
    ["J.L. Simon, P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, J. Laskar, 1994,"
    "'Numerical expressions for precession formulae and mean elements for the Moon and the planets',"
    "A&A, 282, 663 (1994A&A...282..663S)"])

Constant('TROPICALYEAR_J2000DAY', 365.242190402, 'day',
    "Number of days per tropical year",
    ["J.L. Simon, P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, J. Laskar, 1994,"
    "'Numerical expressions for precession formulae and mean elements for the Moon and the planets',"
    "A&A, 282, 663 (1994A&A...282..663S)"])

Constant('ASTRONOMICAL_YEAR', Constant.ALL["SIDEREALYEAR_J2000DAY"].value * 60 * 60 * 24, 's',
    "Astronomical year",
    ["J.L. Simon, P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, J. Laskar, 1994,"
    "'Numerical expressions for precession formulae and mean elements for the Moon and the planets',"
    "A&A, 282, 663 (1994A&A...282..663S)"])

Constant('ASTRONOMICAL_UNIT', 149597870700.0, 'm',
    "Astronomical unit",
    ["IAU, August 2012, 'Re-definition of the astronomical unit of length',"
    "IAU 2012 Resolution B2 adopted at the XXVIII-th General Assembly of the IAU"])

Constant.alias('au', 'ASTRONOMICAL_UNIT')

Constant("GM_SUN", 1.327124400419394e+20, 'm^3/s^2',
    "Sun gravitational parameter",
    ["Table 8 from http://ipnpr.jpl.nasa.gov/progress_report/42-196/196C.pdf"])

Constant("SUN_SCHWARZSCHILD_RADIUS",
    2 * Constant.ALL["GM_SUN"].value / Constant.ALL["c"].value**2, 'm',
    "Sun Schwarzschild radius")

Constant("PARSEC_METER", 3.0856775814913674e+16, 'm',
    "Parsec expressed in meters")

Constant("NEWTON_CONSTANT", 6.674080e-11, 'm^3/kg/s^2',
    "Newton's universal constant of gravitation",
    ["P.J. Mohr, B.N. Taylor, D.B. Newell, 9 July 2015, 'The 2014 CODATA Recommended Values of the Fundamental"
    "Physical Constants', National Institute of Standards and Technology, Gaithersburg, MD 20899-8401;"
    "http://www.codata.org/",
    "http://physics.nist.gov/constants (Web Version 7.0). See also the IAU (2009) System of Astronomical Constants"
    "(IAU, August 2009, 'IAU 2009 Astronomical Constants', IAU 2009 Resolution B2 adopted at the XXVII-th General"
    "Assembly of the IAU. See also IAU, 10 August 2009, 'IAU WG on NSFA Current Best Estimates',"
    "http://maia.usno.navy.mil/NSFA/NSFA_cbe.html)"])

Constant("SUN_MASS", 1.98848e+30, 'kg',
    "Solar mass")
