### Package Management ###

# PIP   //   https://pypi.org/

# py -m pip --install
# py -m pip --version
# py -m pip install numpy

import numpy

numpy_array = numpy.array([5, 11, 45, 32, 56])
print(type(numpy_array))
print(numpy_array)

#  py -m pip install pandas

#import pandas

# py -m pip uninstall pandas
# py -m pip list
# py -m pip show

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())


