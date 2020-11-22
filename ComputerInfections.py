import random
import math


def number_of_days():
    total_days = []
    for _ in range(10000):
        infection_chance = .1
        total_computers = [0] * 100
        total_computers[0] = 1
        days = 0

        probabilities = []  # create a list of random probability values
        for _ in range(len(total_computers)):
            probabilities.append(random.random())  # random values between 0 and 1 inclusive

        while True:
            for i in range(len(total_computers)):
                if probabilities[i] < infection_chance:
                    total_computers[i] = 1
                    infection_chance = 1 - (.9 ** sum(total_computers))
                    days += 1

            if sum(total_computers) > 10:
                for j in range(len(total_computers)):  # technician will repair 10 comps by going down the line
                    count = 0
                    if total_computers[j] == 1:
                        total_computers[j] = 0
                        count += 1
                    if count == 10:  # technician can only repair ten comps
                        break

            if sum(total_computers) <= 10:
                total_days.append(days + 1)
                break

    print(f'The average number of days it takes to '
          f'fully repair the computers is approximately {math.ceil(sum(total_days) / len(total_days))} days.')


number_of_days()
