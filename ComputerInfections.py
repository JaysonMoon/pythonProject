import random

total_days = []


def number_of_days():
    for _ in range(10):
        infection_chance = .1
        total_computers = [0] * 99
        total_computers.append(1)
        days = 0
        a, b = random.choice(list(enumerate(total_computers)))

        probabilities = []  # create a list of random probability values
        for _ in range(100):
            probabilities.append(random.uniform(0, 1))  # random values between 0 and 1 inclusive

        while True:
            for i in range(100):
                if probabilities[i] > infection_chance:
                    total_computers[i] = 1
                    infection_chance = 1 - (.9 ** sum(total_computers))
                    for j in range(100):  # technician will repair 10 comps by going down the line
                        count = 0
                        if total_computers[j] == 1:
                            total_computers[j] = 0
                            count += 1
                        if count == 10:  # technician can only repair first ten comps
                            break
                    days += 1
            if sum(total_computers) < 11:
                total_days.append(days + 1)
                break

    print(f'After 1000 trials, the average number of days it takes to '
          f'fully repair the computers is {sum(total_days) / 10} days.')


number_of_days()
