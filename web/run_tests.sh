# these are executed inside the 'tests' container
python app.py &
python tests.py
nosetests tests/acceptance
