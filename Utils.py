import math, random


# base class for simulator
class GAPoint:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    # find the distance to another object
    def get_distance_to(self, other):
        return math.sqrt(math.pow(self.x_pos - other.x_pos, 2) + math.pow(self.y_pos - other.y_pos, 2))


class Chromosome(GAPoint):
    # x_pos and y_pos are the features of our chromosome
    def __init__(self, x_pos, y_pos):
        self.fitness = 0
        super().__init__(x_pos, y_pos)

    # encode X-Y position into low-level representation
    def encode_position(self):
        pass

    # decode X-Y position from low-level representation
    def decode_position(self):
        pass

    """
    1. create a child from Chromosome x and y positions.
    2. mutate 
    
    """
    def crossover(self, other):
        child = Chromosome(self.x_pos, self.y_pos)
        child.x_pos = ((self.x_pos + other.x_pos) /2)
        child.y_pos = ((self.y_pos + other.y_pos) /2)
        child.mutate()

        return child

    # mutate the individual

    def mutate(self):
        self.x_pos = self.x_pos + random.randint(-5, 5)
        self.y_pos = self.y_pos + random.randint(-5, 5)





class Food(GAPoint):
    def __init__(self, x_pos, y_pos):
        self.amount = 100
        super().__init__(200, 200)

    def reduce_amount(self):
        self.amount -= 1

    def get_amount(self):
        return self.amount

    # respawn food when depleted


    def reposition(self):
        self.amount = 100
        self.x_pos = random.randint(10, 790)
        self.y_pos = random.randint(10, 590)
