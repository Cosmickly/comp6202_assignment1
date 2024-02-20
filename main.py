import random

pop_size = 500
g_length = 28
m_rate = 1 / g_length
tornament_size = 2

template = list("methinks it is like a weasel")


def random_genome(length):
    return "".join((chr(random.randint(32, 126)) for _ in range(length)))


# randrange(a,b) is inclusive a, exclusive b
# randint(a,b) is inclusive a, inclusive b
def mutate_genome(genome):
    genome = list(genome)
    for i in range(len(genome)):
        if random.random() < m_rate:
            genome[i] = chr(random.randint(32, 126))
    return "".join(genome)


def fitness_function(genome):
    fitness = 0
    for i in range(len(genome)):
        if genome[i] == template[i]:
            fitness += 1
    return fitness / g_length


def hill_climber(genome):
    genomes = {genome: fitness_function(genome)}
    while fitness_function(genome) < 1:
        n_genome = mutate_genome(genome)

        if n_genome not in genomes:
            genomes[n_genome] = fitness_function(n_genome)

        if genomes[n_genome] > genomes[genome]:
            genome = n_genome

    return genome


def ga_no_crossover(population):
    genomes = {}
    while True:
        a1 = random.choice(population)  # take 2 random members
        b1 = random.choice(population)

        if a1 not in genomes:
            genomes[a1] = fitness_function(a1)

        if b1 not in genomes:
            genomes[b1] = fitness_function(b1)

        p1 = a1 if genomes[a1] > genomes[b1] else b1  # mutate member with higher fit
        c = mutate_genome(p1)

        a2 = random.randrange(0, pop_size)  # take another 2 members
        b2 = random.randrange(0, pop_size)

        if population[a2] not in genomes:
            genomes[population[a2]] = fitness_function(population[a2])

        if population[b2] not in genomes:
            genomes[population[b2]] = fitness_function(population[b2])

        if genomes[population[a2]] > genomes[population[b2]]:  # replace lower member w/ child
            population[b2] = c
        else:
            population[a2] = c

        if fitness_function(c) >= 1:
            return population


def convert(genome):
    return "".join(genome)


def pp(population):
    for p in population:
        print(p)


if __name__ == '__main__':
    pop = list(random_genome(g_length) for _ in range(pop_size))
    # pp(pop)
    # print(fitness_function(pop[0]))
    # print(pop[0])
    # print(mutate_genome(pop[0]))
    # print(hill_climber(pop[0]))


    pop = ga_no_crossover(pop)
    print(template)
    pp(pop)
