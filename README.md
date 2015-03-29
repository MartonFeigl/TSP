# TSP
Refactoring travelling salesman problem with ant colony simulation in Python

Running the code in Linux Terminal:
$ python tsp.py num citiesAndDistances.pickled out
where num is the number of cities to be visited, and is to be between 2 and 12;
out is an output file into which the results will be written

In order to run the code with a profiling tool, enter the following
into the Linux Terminal:
$ python -m cProfile -s time tsp.py num citiesAndDistances.pickled out
where, again, num is the number of cities to be visited, in between 2 and 12

