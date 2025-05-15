import random
assets = [
    ["Saham 1", 100, 20],
    ["Saham 2", 150, 35],
    ["Saham 3", 200, 40],
    ["Saham 4", 50, 10],
    ["Saham 5", 120, 25],
    ["Saham 6", 180, 30]
]

budget = 350
pop_size = 6
generations = 15
crossover_rate = 0.8
mutation_rate = 0.1

def generate_chromosome():
    return [random.randint(0, 1) for _ in range(len(assets))]

def calculate_fitness(chromosome):
    total_cost = total_return = 0
    for gene, asset in zip(chromosome, assets):
        if gene == 1:
            total_cost += asset[1]
            total_return += asset[2]
    return total_return if total_cost <= budget else 0

def selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    if total_fitness == 0:
        return random.choices(population, k=2)
    probs = [f / total_fitness for f in fitnesses]
    return random.choices(population, weights=probs, k=2)

def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1[:], parent2[:]

def mutate(chromosome):
    return [1 - gene if random.random() < mutation_rate else gene for gene in chromosome]

# Inisialisasi populasi awal
population = [generate_chromosome() for _ in range(pop_size)]

print("=== Populasi Awal ===")
for i, chrom in enumerate(population):
    print(f"{i+1}: {chrom}")

# Proses evolusi
for gen in range(generations):
    fitnesses = [calculate_fitness(chrom) for chrom in population]

    print(f"\n Generasi {gen+1} - Fitness Populasi:")
    for i, fit in enumerate(fitnesses):
        print(f"Individu {i+1}: Fitness = {fit}")

    new_population = []
    while len(new_population) < pop_size:
        parent1, parent2 = selection(population, fitnesses)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.extend([child1, child2])

    population = new_population[:pop_size]

# Evaluasi solusi terbaik
best = max(population, key=calculate_fitness)
best_fitness = calculate_fitness(best)

print("\n Solusi Terbaik:")
print(f"Kromosom: {best}")
print("Aset Terpilih:")
total_cost = total_return = 0
for gene, asset in zip(best, assets):
    if gene == 1:
        print(f"- {asset[0]} (Biaya: {asset[1]}, Return: {asset[2]})")
        total_cost += asset[1]
        total_return += asset[2]
print(f"Total Biaya: {total_cost}")
print(f"Total Return: {total_return}")
print(f"Fitness: {best_fitness}")
