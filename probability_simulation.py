'''
In "Elementary Statistics by Mario F. Triola, I came across a section
delving into probability simulation. They wrote, "There is a right way
to simulate rolling a pair of dice and a wrong way. The right way is to
randomly generate two numbers 1-6, then add them. The wrong way is to 
generate one number 2-12. I wanted to understand what the difference 
was, so I wrote this program to compare the two ways.
'''

import numpy as np
from matplotlib import pyplot as plt


def main():
    # Set number of simulations 
    N = 2_000

    # Simulation A
    resultsA = []
    resultsB = []
    for _ in range(N):
        batchA = np.random.randint(1,7,size=2)
        batchA_Sum = np.sum(batchA)
        resultsA.append(batchA_Sum)

        batchB = np.random.randint(2,13,size=1)
        resultsB.append(batchB[0])

    # Count occurrences of numbers in the lists
    max_size = max(max(resultsA), max(resultsB)) + 1
    
    #countA = [resultsA.count(i) for i in range(max_size)]
    #countB = [resultsB.count(i) for i in range(max_size)]

    countA = []
    countB = []
    for i in range(max_size):
        countA.append(resultsA.count(i))
        countB.append(resultsB.count(i))

    # Create the figure and subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.bar(range(len(countA)), countA, width=0.8, align='center')
    ax2.bar(range(len(countB)), countB, width=0.8, align='center')
    ax1.set_title(f'Simulation A: Summing 2 Randomly Generated Dice, N = {N}')
    ax2.set_title(f'Simulation B: Randomly Generating Number Between 2-12, N = {N}')
    ax1.set_ylabel('Occurrences')
    ax2.set_ylabel('Occurrences')
    ax2.set_xlabel('Sum of Dice')
    plt.savefig('probability_simulation.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()