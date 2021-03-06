
import random
import sys
import Work


class BigGroup:
    def __init__(self, graph, num_ants, num_iterations):
        self.graph = graph
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.Alpha = 0.1
        self.reset()

    def reset(self):
        self.bestPathCost = sys.maxint
        self.bestPathVector = None
        self.bestPathMatrix = None
        #self.lbpi = 0

    def start(self):
        self.ants = self.c_workers()
        self.iter_counter = 0

        while self.iter_counter < self.num_iterations:
            self.iteration()
            # Note that this will help refine the results future iterations.
            self.global_updating_rule()

    def iteration(self):
        self.avg_path_cost = 0
        self.ant_counter = 0
        self.iter_counter += 1
        for ant in self.ants:
            ant.run()

    def num_ants(self):
        return len(self.ants)

    def num_iterations(self):
        return self.num_iterations

    def iteration_counter(self):
        return self.iter_counter

    def update(self, ant):
        #print "Update called by %s" % (ant.ID,)
        self.ant_counter += 1
        self.avg_path_cost += ant.path_cost
        if ant.path_cost < self.bestPathCost:
            self.bestPathCost = ant.path_cost
            self.bestPathMatrix = ant.path_mat
            self.bestPathVector = ant.path_vec
            #self.lbpi = self.iter_counter
        if self.ant_counter == len(self.ants):
            self.avg_path_cost /= len(self.ants)
            print "%02d: best path vector: %s, best path cost: %d, avg path cost: %d" % (
                self.iter_counter, self.bestPathVector, self.bestPathCost, self.avg_path_cost,)


    def done(self):
        return self.iter_counter == self.num_iterations

    def c_workers(self):
        self.reset()
        ants = []
        for i in range(0, self.num_ants):
            ant = Work.Work(i, random.randint(0, self.graph.num_nodes - 1), self)
            ants.append(ant)

        return ants

    def global_updating_rule(self):
        #can someone explain this
        evaporation = 0
        deposition = 0
        for r in range(0, self.graph.num_nodes):
            for s in range(0, self.graph.num_nodes):
                if r != s:
                    delt_tau = self.bestPathMatrix[r][s] / self.bestPathCost
                    evaporation = (1 - self.Alpha) * self.graph.tau(r, s)
                    deposition = self.Alpha * delt_tau
                    self.graph.update_tau(r, s, evaporation + deposition)

