# Integer - 17. 999 dan katta  bo`lgan son berilgan. Bir marta bo`lib butunni 
#va bo`lib qoldiqni olish  operatsiyasidan foydalanib berilgan sonni yuzliklar 
#xonasidagi sonni aniqlovchi  programma tuzilsin.

A=int(input('999 dan katta son kiriting = '))
B = A // 1000
C= A % 1000
D = C // 100
print('Butun son B= ', B, 'yuzliklar xonasidagi son D= ', D)




'''B = A//100
C = (A//10)%10
D = A%10'''