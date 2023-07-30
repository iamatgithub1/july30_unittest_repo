import os
from os.path import dirname as up


cwd = os.getcwd()
print(cwd)
two_up = up(up(__file__))
print(two_up)
one_up = up(__file__)
print(one_up)