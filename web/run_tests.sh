#!/bin/bash

# these are executed inside the 'tests' container

# set flask log level to error to suppress unnecessary output to py.test stdout
FLASK_LOG_LEVEL=ERROR python app.py &

# output results to junit-style xml
mkdir -p build
py.test -v --junitxml build/junit.xml
