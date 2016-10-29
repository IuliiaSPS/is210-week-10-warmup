#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_03"""


import data


CORRECTED = data.BANDS.copy()

CORRECTED['Dylan'] = {'Bob Dylan': ['vocal', 'metal', 'harmonica']}

del CORRECTED['Van Halen']['David Lee Roth']

CORRECTED['Van Halen'] = {'Sammy Hagar': ['vocals']}

print CORRECTED
