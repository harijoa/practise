x = int(input('enter a number')
for i in range(2,x):
  if x % i == 0:
    print(x,'is not a prime number')
    print(i,'is',x//i,'is equal to',x)      #  it will show divisible number as well as how many times it'll divisible to that number
    break
else:
  print(x,'is a prime number')
