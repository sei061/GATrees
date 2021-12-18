import copy
import random, math
from Utils import Chromosome, Food, GAPoint


class GAEngine:

    def __init__(self):
        self.population = []
        self.food = []
        self.generations = 0

    def make_initial_population(self, population_size):
        for i in range(population_size):
            self.population.append(Chromosome(random.randint(0, 790), random.randint(0, 590)))

    def add_food(self, no_of_food):
        for i in range(no_of_food):
            self.food.append(Food(random.randint(0, 790), random.randint(0, 590)))


    """
    1. split the population in half as I decided to use elitist selection.
    2. for the selected half, the two best parents create an offspring that replaces the least fit offspring.
    """
    def do_crossover(self, list_of_offspring):

        half = int(len(self.population) / 2)
        self.population[:half]

        for i in range(half):
            self.population[len(self.population)-1] = self.population[i].crossover(self.population[i+1])

    # fitness calculation goes here...
    """
    1. For each member in the population, assign it a fitness value.
    2. set fitness as the distance between the member and the food.
    3. Sort the population by fitness value 
    """
    def assign_fitness(self):
        for i in self.population:
            i.fitness = self.food[0].get_distance_to(i)

        self.population.sort(key=lambda p: p.fitness)








    def get_population(self):
        return self.population

    def get_foods(self):
        return self.food


