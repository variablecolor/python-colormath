# -*- coding: utf-8 -*-
"""
Contains lookup tables, constants, and things that are generally static
and useful throughout the library.
"""

import numpy

# Not sure what these are, they are used in Lab and Luv calculations.
CIE_E = 216.0 / 24389.0
CIE_K = 24389.0 / 27.0

# Observer Function and Illuminant Data
ILLUMINANTS = {
    # 2 Degree Functions
    '2': {
        'a': (1.09850, 1.00000, 0.35585),
        'b': (0.99072, 1.00000, 0.85223),
        'c': (0.98074, 1.00000, 1.18232),
        'd50': (0.96422, 1.00000, 0.82521),
        'd55': (0.95682, 1.00000, 0.92149),
        'd65': (0.95047, 1.00000, 1.08883),
        'd75': (0.94972, 1.00000, 1.22638),
        'e': (1.00000, 1.00000, 1.00000),
        'f2': (0.99186, 1.00000, 0.67393),
        'f7': (0.95041, 1.00000, 1.08747),
        'f11': (1.00962, 1.00000, 0.64350)
    },
    # 10 Degree Functions
    '10': {
        'a': (1.11142, 1.00000, 0.3519978),
        'b': (0.99177, 1.00000, 0.84349),
        'c': (0.97286, 1.0, 1.16145),
        'd50': (0.96720, 1.00000, 0.81427),
        'd55': (0.958, 1.00000, 0.9093),
        'd65': (0.94811, 1.00000, 1.07304),
        'd75': (0.94416, 1.00000, 1.2064),
        'e': (1.00000, 1.00000, 1.00000),
        'f2': (1.03245, 1.0, 0.68990),
        'f7': (0.95780, 1.0, 1.07618),
        'f11': (1.038197, 1.0, 0.6556)
    }
}

OBSERVERS = ILLUMINANTS.keys()

# Chromatic Adaptation Matrices
# http://brucelindbloom.com/Eqn_ChromAdapt.html
ADAPTATION_MATRICES = {
    'xyz_scaling': numpy.array((
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0))),
    'bradford': numpy.array((
        (0.8951, 0.2664, -0.1614),
        (-0.7502, 1.7135, 0.0367),
        (0.0389, -0.0685, 1.0296))),
    'von_kries': numpy.array((
        (0.40024, 0.70760, -0.08081),
        (-0.22630, 1.16532, 0.04570),
        (0.00000, 0.00000, 0.91822))),
}
