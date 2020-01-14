# germanetpy
Welcome. This is the Python API for the German wordnet GermaNet. GermaNet is a lexical-semantic net that relates German nouns, verbs, and adjectives semantically by grouping lexical units that express the same concept into synsets and by defining semantic relations between these synsets.
This API can be used to extract structured information from the GermaNet with python.
More information about GermaNet can be found on the following page:

https://uni-tuebingen.de/en/faculties/faculty-of-humanities/departments/modern-languages/department-of-linguistics/chairs/general-and-computational-linguistics/ressources/lexica/germanet/

##Installation

You can install germanetpy from [PyPI] (https://pypi.org/project/germanetpy/):

    pip install germanetpy

Get the GermaNet data as XML files and put all files in the data directory. The API is supported on Python 3.

##How to use

The API provides functionality that can be used to load the data from GermaNet and query it. The data has to be retrieved
via a license agreement from the University of Tübingen, Seminar für Sprachwissenschaften:

https://uni-tuebingen.de/en/faculties/faculty-of-humanities/departments/modern-languages/department-of-linguistics/chairs/general-and-computational-linguistics/ressources/lexica/germanet/license/

This repository also provides a Tutorial [germanetpy_tutorial.ipynb] that shows how to use the API to query GermaNet.