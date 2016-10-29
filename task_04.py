#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_04"""


import data

data.BANDS.update({'Buckingham Nicks':
                   {'Lindsey Buckingham': ['guitar', 'vocals'],
                    'Stevie Nicks': ['vocals', 'tambourine']}})

data.BANDS['Fleetwood Mac'].update({'Lindsey Buckingham': ['guitar', 'vocals'],
                                    'Stevie Nicks': ['vocals', 'tambourine']})
print data.BANDS
