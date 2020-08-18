x = int(input('Enter a number upto'))
if x == 2:
  print(2,'is a prime number')
else:
  for i in range(2,x+1):
    for j in range(2,i):
      if (i % j) == 0:
        print(i,'is not a prime number')
        break
    else:
      print(i,'is a prime number')
