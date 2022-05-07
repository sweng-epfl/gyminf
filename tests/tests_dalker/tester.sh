ln -sf ../cours/*.py .
coverage run -m unittest test_functions.py test_pizza.py
coverage report
