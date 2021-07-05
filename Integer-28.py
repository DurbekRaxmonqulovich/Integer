# Integer-28. Hafta kunlari  quyidagicha tartibda berilgan. 1-dushanba, 2-seshanba, 
#3-chorshanba,  4-payshanba, 5-juma, 6-shanba, 7-yakshanba(N 1-7gacha bo`lgan 
#hafta kunlari  soni). 1-365 oraliqda yotuvchi K soni berilgan. Agar 1-yanvar 
#N chi kunga  to`g`ri kelsa, kiritilgan K - kun haftaning qaysi kuniga to`g`ri 
#kelishini  aniqlovchi programma tuzilsin.
K=int(input('1...365 gacha bulgan bitta son kiriting= '))
kunlar= {0: 'якшанба', 1: 'душанба', 2: 'сешанба', 3: 'чоршанба', 4: 'пайшанба', 5: 'жума', 6: 'шанба' }
if 1<=K<=365:
    i = (K+6)%7
print("Сиз киритган йилнинг раками: ", K)
print("Хафта раками: ", i)
print("Хафта номи:",kunlar[i])

#????????????????????????????????????????????????????????????????
            ISHLANMAGAN