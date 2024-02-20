import random

pop_size = 500
g_length = 28
m_rate = 1 / g_length
tournament_size = 2

template = "methinks it is like a weasel"


def convert(genome):
    return "".join(genome)


def pp(population):
    for p in population:
        print(p)

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
    generations = 0
    while True:
        sample = random.sample(population, 2)  # take 2 members
        a, b = sample[0], sample[1]

        for x in sample:
            if x not in genomes:
                genomes[x] = fitness_function(x)

        p1 = a if genomes[a] > genomes[b] else b  # mutate member with higher fit
        c = mutate_genome(p1)

        sample = random.sample(range(len(population)), 2)  # take another two members
        a, b = sample[0], sample[1]

        for x in sample:
            if population[x] not in genomes:
                genomes[population[x]] = fitness_function(population[x])

        if genomes[population[a]] > genomes[population[b]]:  # replace lower member w/ child
            population[b] = c
        else:
            population[a] = c

        generations += 1
        if fitness_function(c) >= 1:
            print(f"Generations: {generations}")
            return population


def crossover(p1, p2):
    c = []
    for i in range(len(p1)):
        if random.random() > 0.5:
            c.append(p1[i])
        else:
            c.append(p2[i])
    return "".join(c)


def ga_crossover(population):
    genomes = {}
    generations = 0
    while True:
        sample = random.sample(population, 4)  # take four members
        a1, b1, a2, b2 = sample[0], sample[1], sample[2], sample[3]

        for x in sample:
            if x not in genomes:
                genomes[x] = fitness_function(x)

        p1 = a1 if genomes[a1] > genomes[b1] else b1  # highest fitness for each
        p2 = a2 if genomes[a2] > genomes[b2] else b2

        c = mutate_genome(crossover(p1, p2))

        sample = random.sample(range(len(population)), 2)  # take another two members
        a, b = sample[0], sample[1]

        for x in sample:
            if population[x] not in genomes:
                genomes[population[x]] = fitness_function(population[x])

        if genomes[population[a]] > genomes[population[b]]:  # replace lower member w/ child
            population[b] = c
        else:
            population[a] = c

        generations += 1
        if fitness_function(c) >= 1:
            print(f"Generations: {generations}")
            return population


if __name__ == '__main__':
    pop = list(random_genome(g_length) for _ in range(pop_size))

    pop = ga_crossover(pop)  # gens = 9730 - 23000
    # pop = ga_no_crossover(pop)  # gens = 50000 - 90000
    pp(pop)

