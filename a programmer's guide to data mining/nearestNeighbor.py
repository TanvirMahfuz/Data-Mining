from manhattenDistance import ManhattanDistance
def computeNearestNeighbor(username,users):
  distances =[]
  for user in users:
    '''counting distances from the username to every other user'''
    if user != username:
      distance = ManhattanDistance(users[user], users[username])
      distances.append((distance, user))
  distances.sort()
  return distances