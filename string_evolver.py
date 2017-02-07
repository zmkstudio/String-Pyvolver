import time
import string
import random

start_time = time.time()

string = "aqotkf,vkhlqode"
target = "Zach Komorowski"

def fitness(target, string):
    fitness = 0
    for i in range(0, len(target)):
        fitness += (ord(target[i]) - ord(string[i]))**2         #compares character at position i in target string with test string
    return fitness

def randomParent(size=len(target), chars=string.upper() + string.lower()):
    return ''.join(random.choice(chars) for i in range(size))

def crossover(string):
    parent1 = string
    parent2 = randomParent()

    cross_pos = random.randint(0, len(string))

    parent1_list = list(parent1)
    parent2_list = list(parent2)

    half_parent1 = ''.join(parent1_list[0:cross_pos])
    half_parent1 = list(half_parent1)

    half_parent2 = ''.join(parent2_list[cross_pos:len(parent1)])
    half_parent2 = list(half_parent2)

    child = ''.join(half_parent1 + half_parent2)

    return child

def mutate(string):
    m_pos = random.randint(0, len(string) - 1)
    # child = string.replace(string[m_pos])

    parts = list(string)
    # child = string.replace(string[random.randrange(len(string))], chr(random.randrange(97, 97 + 26 + 1)), 1)
    # child = string.replace(string[m_pos], chr(random.randrange(97, 97 + 26 + 1)), 1)
    parts[m_pos] = chr(ord(parts[m_pos]) + random.randint(-1, 1))
    child = ''.join(parts)
    return child

def genPop():
    x = 0
    population = []
    for i in range(10):
        population.append(randomParent())
        i += 1

    return population

fit_val = fitness(target, string)
i = 0
print "\tGen\t String\t\t\t\t Fitness"
print "\t%i\t %s\t\t %i" %(i, string, fit_val)

prev_gen_fit = 0
prev_gen_string = ""

while True:
    i += 1
    prev_gen_fit = fit_val
    prev_gen_string = string

    # string = crossover(string)
    string = mutate(string)
    fit_val = fitness(target, string)

    if (fit_val > prev_gen_fit):
        fit_val = prev_gen_fit
        string = prev_gen_string

    if (fit_val != prev_gen_fit):
        print "\t%i\t %s\t\t %i" %(i, string, fit_val)

    if (fit_val == 0):
        break
    # if (i > 5000):
    #     break

print "\n\nGenerations run: %i" %i
print "\n\nRuntime: %.10fs" %(time.time() - start_time)
