"""
Licensed under CC Attribution http://creativecommons.org/licenses/by/3.0/
Copyright 2011, Steve Engledow
"""

def do_round(votes, counts = {}, loser=None):
    for vote in votes:
        for i in range(len(vote)):
            if not loser:
                if vote[i] not in counts:
                    counts[vote[i]] = 0
                counts[vote[i]] += 1
                break
            else:
                if vote[i] == loser:
                    for j in range(i+1, len(vote)):
                        if vote[j] in counts:
                            counts[vote[j]] += 1
                            break
                    break
                elif vote[i] in counts:
                    break

    print counts

    # determine if there's a winner
    total = sum(counts.values())
    for choice in counts:
        if counts[choice] > total / 2:
            print choice, "wins!"
            return

    # otherwise, find the loser
    loser = None
    for choice in counts:
        if not loser or counts[choice] < counts[loser]:
            loser = choice
    print loser, "loses"
    del counts[loser]
    do_round(votes, counts, loser = loser)

import sys
if len(sys.argv) != 2:
    print "Expected a filename as the sole argument."
    print "The file should be a space-separated list of vote preferences with each ballot separated by a newline."
else:
    votes = []
    f = open(sys.argv[1], 'r')
    for line in f:
        votes.append(line.split())
    f.close()

    do_round(votes)
