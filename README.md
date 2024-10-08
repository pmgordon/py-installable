# Python cmd

This repository contains example use cases for various tasks that can be covered with pytest

## Installation

* Fork or Clone this repo
* Make a python virtual environment at .pyenv -> `make init`
* Source the python virtual environment `source .pyenv/bin/activate`
* Install requirements `make pipreq` 


## Test
### Run All Tests
To run all tests execute `make test`

### Coverage Report
To run all tests execute `make coverage`


# Installation

### Install command from package

Install
```
pip install . 
```
Uninstall
```
pip uninstall cli-command   
```

### Install from github

Install

```
pip install git+https://github.com/pmgordon/py-installable
```

Install Specific version
```
pip install git+https://github.com/pmgordon/py-installable@0.1.0
```

Uninstall
```
pip uninstall cli-command 
```

## Test
Run the command
```
(.pyenv) paul:py-installable/ (main) $ py-command                                                                                                                                       [11:26:35]
This is the main
```