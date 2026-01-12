points = [[1,1],[3,4],[-1,0]]


def minTimeToVisitAllPoints(pointsArr):
  time = 0
  
  for index in range(len(pointsArr) -1):
    [x,y] = pointsArr[index]
    [x_n,y_n] = pointsArr[index+1]
    # trick
    count = max(abs(x_n - x), abs(y_n - y))
    time+=count


  return time



print(minTimeToVisitAllPoints(points))