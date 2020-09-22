tal_1 = 0
for i in range(10):
    tal_1 += 1
    print(tal_1)

tal_2 = []
tal = 0
for i in range(50):
    tal += 1
    tal_2.append(tal)

print(tal_2[0:len(tal_2):2])

tal_3 = 11
for i in range(10):
    tal_3 -= 1
    print(tal_3)

tal_4 = []
talo = 6
for i in range(993):
    talo += 1
    tal_4.append(talo)


print(sum(tal_4))

import math

tal_5 = []
talt = 0
for i in range(1000):
    talt += 1
    tal_5.append(talt)

print(math.prod(tal_5))