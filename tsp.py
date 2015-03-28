
import BigGroup
import GraphBit

import pickle
import sys
import traceback


def main(argv):
    numberOfNodes = 10

    if len(argv) >= 3 and argv[0]:
        numberOfNodes = int(argv[0])

    if numberOfNodes <= 10:
        numberOfAnts = 20
        numberOfIterations = 12
        #nr = 1
    else:
        numberOfAnts = 28
        numberOfIterations = 20
        #nr = 1

    input_arguments = pickle.load(open(argv[1], "r"))
    cities = input_arguments[0]
    numOfCities = input_arguments[1]
    #why are we doing this? In order to taylor the numberOfNodes to the numOfCities
    if numberOfNodes < len(numOfCities):
        numOfCities = numOfCities[0:numberOfNodes]
        for i in range(0, numberOfNodes):
            numOfCities[i] = numOfCities[i][0:numberOfNodes]



    try:
        graph = GraphBit.GraphBit(numberOfNodes, numOfCities)
	bestPathVector = None
        bestPathCost = sys.maxint
        #for i in range(0, nr): --- removed, for nr is always one
        print "Repetition %s" % i
        graph.reset_tau()
        workers = BigGroup.BigGroup(graph, numberOfAnts, numberOfIterations)
        print "Colony Started and running well"
        workers.start()
        if workers.bestPathCost < bestPathCost:
             print "Colony Path"
             bestPathVector = workers.bestPathVector
             bestPathCost = workers.bestPathCost

        print "\n------------------------------------------------------------"
        print "                     Results                                "
        print "------------------------------------------------------------"
        print "\nBest path = %s" % (bestPathVector,)
        city_vec = []
        for node in bestPathVector:
            print cities[node] + " ",
            city_vec.append(cities[node])
        print "\nBest path cost = %s\n" % (bestPathCost,)
        results = [bestPathVector, city_vec, bestPathCost]
        pickle.dump(results, open(argv[2], 'w+'))
    except Exception, e:
        print "exception: " + str(e)
        traceback.print_exc()


if __name__ == "__main__":
    main(sys.argv[1:])
