# github-cli
A github command line interface written in Python. This script is using Github Rest API V3.

[![Build Status](https://semaphoreapp.com/api/v1/projects/d4cca506-99be-44d2-b19e-176f36ec8cf1/128505/shields_badge.svg)](https://semaphoreapp.com/boennemann/badges)
[![GitHub version](https://badge.fury.io/gh/boennemann%2Fbadges.svg)](http://badge.fury.io/gh/boennemann%2Fbadges) [![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
### Requirements
* Python 3.x
* colorama python package
* tabulate python package
* requests python package

__Currently we are not created proper package for the script as it is in development status. Once it is completed will be uploaded__

### Features

* Search for any user on the github and return with information about that user
* Search repo for a specific user and get information about the repo
* If the repo is forked from somewhere it will tells about the original owner

### Usage

On Windows

`python github.py <username>`

`python github.py <username> <reponame>`

On Linux

`python github.py <username>`

`python github.py <username> <reponame>`

__After its development is complete we create a proper package then we dont have to write python before and .py with the file name__

### Screenshots

![alt text](http://i65.tinypic.com/nqehhv.jpg "Getting user information")


![alt text](http://i68.tinypic.com/10cknk2.jpg "Getting repo information")


### Contribute

Just fork the repo, make changes, test and then send the pull request. 






