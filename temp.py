#%%
num = int(input('please ennter a number:'))

if num % 2 != 0:
    print('your num is fard')
else:
    print('your num is zoj')
#%%
num = int(input('please enter tool zele:'))
print(num*' #')
counter = (num-1)
print()
while counter >= 1:
    if counter  > 1:
        print((num*' #'))
        print((num) * ' ')
      
    
    elif counter == 1:
        print(num*' #')
    counter -= 1
#%%
num = int(input('please enter tool zele:'))
counter = num
while counter >= 1:
    if counter == num:
        print((num*' #'))
    elif counter == 0:
        print(num*' #')
        
    elif counter >= (num-1) & counter <=1:
        print(f' # {(num-2)*"  "}#')
    
    counter -= 1
print(num*' #')
#%%
num=int(input('plaese enter a number:'))
a = 0
b = 1
print(a)
print(b)
for i in range(num+1):
    sum_num = a + b
    a = b
    b = sum_num
    print(sum_num)
#%%
name = input('please enter an name:')
print(name[0:len(name):2])
