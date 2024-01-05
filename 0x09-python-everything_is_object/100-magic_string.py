#!/usr/bin/python3
magic_string = lambda x=[0]: 'BestSchool, ' * x[0] + 'BestSchool$' if x.__setitem__(0, x[0] + 1) is None else ''
