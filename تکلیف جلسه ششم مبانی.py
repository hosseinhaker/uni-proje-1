#%% shesh joft addad begirad va har joft ra be tavan ham berasanad
number = 0
while number < 12:
    num_lst = [] 
    counter = 0
    while counter <2:
        num = int(input('please enter a number'))
        number += 1
        counter += 1
        num_lst.append(num)
    if num_lst[1] == 1:
        print(num_lst[0])
    else:
        nums = 1
        for i in range(num_lst[1]):
            nums = nums*num_lst[0]
        print(nums)
#%% tedad kelas yek daneshgah ra daryaft va nomarat danshjooha ra ham daryaft va miangin nomre har klas va miangin nomre daneshgah ra ham bedahad 
nomre_uni = 0
clas = int(input('number class:'))
for clases in range(clas):
    stu = int(input('tedad daneshjoo:'))
    sum_nomre = 0
    for stu_num in range(stu):
        nomre = int(input('nomre daneshjoo:'))
        sum_nomre += nomre
    nomre_clasi = sum_nomre / stu
    nomre_uni += nomre_clasi
    print(f"miangin nomarat daneshjooyan har class:{nomre_clasi}")
miangin_uni = nomre_uni / clas
print(f"miangin nomarat danshjooyan dar kol:{miangin_uni}")







