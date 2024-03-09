#%%  donbale fibonachi ba tabe def
def fibo(nums):
    x=0
    y=1
    count = 0
    if nums <= 0:
        print("Please enter a add mosbat:")
    elif nums == 1:
        print(x)
    else:
        while count < nums:
            print(x)
            z = x + y
            x = y
            y = z
            count += 1
print(fibo(30))
#%% barname benevis ke 5000 addad begire va addad aval ro joda kone bad anharo baham jamkone
count = 2
nums_dic = []
for num in range(1, 5001):
   if num > 1:
       for i in range(2, num):
           if num % i == 0:
               break
       else:
           nums_dic.append(num)
print(nums_dic)    
print(sum(nums_dic))            
print((sum(nums_dic))/(len(nums_dic)))            
#%% nam daneshjooyan ro begirim va tedad karackter kol ra yafte va tedad tekrar har krakter ra begoyad
nam_lst = []
name = ''
while name != 'end':
    name=input('please enter stu names:')
    nam_lst.append(name)        
    print(len(name))
print(nam_lst)
count_num = 0
for ckar in nam_lst:
    for i in nam_lst[(len(name)+1)]:
        count_num += 1        
print(count_num)
























