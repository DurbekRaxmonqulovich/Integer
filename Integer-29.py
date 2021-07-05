#Integer29. A,B,C butun  sonlar berilgan. Tomonlari A va B bo`lgan to`g`ri to`rtburchakka 
#tomoni C  bo`lgan kvadrat eng ko`p joylashtirilsin. To`g`rito`rt burchakka eng ko`p  
#joylashgan kvadratlar soni va joylashmay qolgan qismi yuzasini aniqlovchi  programma 
#tuzilsin.
a=int(input('a-ni kiriting:  '))
b=int(input('b-ni kiriting:  '))
c=int(input('c-ni kiriting:  '))
n=(a//c)*(b//c)
print('joylashgan kvadratlar soni: = ', n)
print('Ortib qolgan yuza: ', a*b-n*c)
'''s1 = a * b
s2 = c * c
c = s1 // s2
c1 = s1 % s2
print('joylashgan kvadratlar soni: = ', c)
print('joylashmagan kvadratlar soni: = ', c1) ХАТОООООООО'''
