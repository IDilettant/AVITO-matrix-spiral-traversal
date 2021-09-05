# Mattrav

[![Maintainability](https://api.codeclimate.com/v1/badges/3535a537d8ebbc6ce79c/maintainability)](https://codeclimate.com/github/IDilettant/AVITO-matrix-spiral-traversal/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3535a537d8ebbc6ce79c/test_coverage)](https://codeclimate.com/github/IDilettant/AVITO-matrix-spiral-traversal/test_coverage)
![Actions Status](https://github.com/IDilettant/AVITO-matrix-spiral-traversal/workflows/tests%20and%20lints/badge.svg)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)


## Description
Mattrav (MATrix TRAVersal) is a library that provides functionality that allows to download 
and process square matrices of a certain format by traversing their values in a spiral: 
counterclockwise, starting from the upper left corner

The library was implemented in accordance with the test assignment for an internship as a back-end developer from Avito

## Features
- Getting matrix from a remote server and providing it in text representation
- Formatting graphical representation of the downloaded matrix to list of lists
- Collecting matrix values traversing in a spiral

## Installation
```bash
pip install git+https://github.com/IDilettant/AVITO-matrix-spiral-traversal.git
```

## Usage
```python
from mattrav import get_matrix

traversal_result = get_matrix(server_url)
```

## Usage examples
