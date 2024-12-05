def minkwoskiDistance(rating1, rating2,r):
  distance = 0
  commonratings = False 
  for key in rating1:
    if key in rating2:
      distance+=pow(abs(rating1[key]-rating2[key]),r)
      commonratings = True
  if commonratings:
    return pow(distance,1/r)
  else :
    return 0