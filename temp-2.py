#%% addad hadaghal 5 raghami begir va agar tedad arghamash fard bood ragham vasat ra neshan dahad va zoj ya fard boodan addad ra begooyad
num = input('please enter a number:')
while len(num) <  5 :
    num = input('please enter a number:')
if (len(num)) % 2 == 0:
    print('your num is zoje')
else:
    print('your num is fard')
    x = int(len(num)/2)
    print(num[x])
#%% برنامه بنویسید که رایانه به طور خودکار یک عدد تولید کند در رنج 1الی20 و کاربر حدس بزند که عدد انتخابی کامپیوتر چه عددی است و تا زمانی که عدد را درست حدس نزند بازی ادامه یابد و همچنین رایانه باید به کاربر راهنمایی های لازم برای حدس عدد را انجام بددهد
import random
counter=0
num = random.randint(1,20)
number = 0
while number != num:
    number = int(input('please enter a number:'))
    counter+=1
    if number < num:
        print('addad koochack')
    else:
        print('addad bozorg')
    
    if counter == 10:
        print('game over')
        break
else:    
    print(f'batedad khatay={counter} barande shodid')
#%%  tedad espeis ha ra bedahad  (ostad gof hesab nist )
my_titr = "mamad ali ra be lam pesht davat kard"
my_titr.count(" ")
#%%  tedad espeis ha ra bedahad 
my_titr = input("jomle khodra vared namaead:")
counter = 0
for i in range (len(my_titr)):
    if my_titr[i] == (" "):
        counter+=1
print(counter)
#%%
import random
counter=0
num = int(input('please enter a number in range 1 , 20 :'))
number = 0
while number != num:
    number = random.randint(1, 20)
    counter+=1
    if num < number:
        print('addad koochack')
    else:
        print('addad bozorg')
    
    if counter == 10:
        print('game over')
        break
else:    
    print(f'batedad khatay={counter} barande shodid')
#%%
