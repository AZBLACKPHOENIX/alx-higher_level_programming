#!/usr/bin/python3
magic_string = lambda x=[0]: 'BestSchool' + ', BestSchool' * x[0] if x.__setitem__(0, x[0] + 1) is None else ''
