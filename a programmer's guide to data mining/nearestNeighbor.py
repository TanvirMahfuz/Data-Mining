from manhattenDistance import ManhattanDistance
from minkwoskiDistance import minkwoskiDistance
def computeNearestNeighbor(username,users):
  distances =[]
  for user in users:
    '''counting distances from the username to every other user'''
    if user != username:
      distance = minkwoskiDistance(users[user], users[username],2)
      distances.append((distance, user))
  distances.sort()
  return distances