import random
number_of_streaks = 0
for experiment_number in range(1000):
    flips = []
    streak_counter = 1
    for i in range(100):
        flips.append('H' if random.randint(0, 1) == 0 else 'T')
    #print(flips)
    for k in range(len(flips) - 1):
        if flips[k] == flips[k+1]:
            streak_counter += 1
        else:
            streak_counter = 1

        if streak_counter == 6:
            number_of_streaks +=1
            break
print('Chance of streak: %s%%' % (number_of_streaks / 1000*100))
