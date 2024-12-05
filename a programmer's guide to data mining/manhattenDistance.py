def ManhattanDistance(ratings1, ratings2):
    distance = 0
    for key in ratings1:
        if(key in ratings2):
            distance += abs(ratings1[key] - ratings2[key])
    return distance