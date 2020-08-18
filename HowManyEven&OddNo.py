x = int(input('length of the array: '))
list = []
for i in range(1,x+1):
    y = int(input('enter a value: '))
    list.append(y)
print(list)
def even_odd(x):
    even = 0
    odd = 0
    for i in list:
        if i % 2 == 0:
          even +=1
        else:
          odd +=1
    
     return even, odd
res1,res2 = even_odd(list)
print('even: {} and odd: {}'.format(res1,res2))
