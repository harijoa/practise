x = int(input('how many term you want?'))
n1,n2 = 0,1
if x > 1:
  print(0)
  print(1)
for i in range(3,x+1):
  nth = n1 + n2
  print(nth)
  n1 = n2
  n2 = nth
