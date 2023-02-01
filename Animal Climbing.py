# an animal climbs on a wall, it starts at the bottom and climbs n meters a day. Everynight it slides m meter down, how many days?
import sys
for line in sys.stdin:
  print(line, end="")
  numbers=line.split()
  n=int(numbers[0])
  m=int(numbers[1])
  H=int(numbers[2])
def climb(n,m,H):
  days=0 
  left=H
  s=True
  if n>=H:
    days+=1
    return days
  elif m>=n:
    return 'Fail'
  else:
    while s:
      if left<=n:
        days+=1
        s=False
      else:
        days+=1
        left-=n
        left+=m
  return days
