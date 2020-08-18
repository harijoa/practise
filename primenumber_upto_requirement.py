x = int(input('how many term you want?')
for i in range(2,x+1):
  prime = True
  for c in range(2,i):
    if i % c == 0:
      prime = False
      break
  if prime == True:
      (i,'is a prime number')
