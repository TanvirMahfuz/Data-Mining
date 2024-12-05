from data import userData
from nearestNeighbor import computeNearestNeighbor
user = input()
nearest = computeNearestNeighbor(user,userData())[0][1]
neighborRatings = userData()[nearest]
userRatings = userData()[user]
recommendations = []
for artist in neighborRatings:
    if artist not in userRatings:
        recommendations.append((artist, neighborRatings[artist]))

print(sorted(recommendations, key=lambda recommendation: recommendation[1], reverse=True))