x = input("Klub A : " )
y = input("Klub B : " )
sepak = [x, y ]
pemenang = []
match = 1
poin_x = 0
poin_y = 0
while True:
    a, b = map(int, input("Pertandingan {} : " .format(match)).split(" "))
    if (a >= 0) and (b>= 0):
        if a  > b :
            pemenang.extend(["Hasil {0} : {1}" .format(match, sepak[0])])
            poin_x += 1
        elif  a < b:
            pemenang.extend(["Hasil {0} : {1}" .format(match, sepak[1])])
            poin_y += 1
        elif a == b:
            pemenang.extend(["Hasil {} : Draw" .format(match)])
    else:
       break
    match += 1


for z in pemenang:
    if x in pemenang:
        print(x ,end="")
        print(" ")
        

    if  y in pemenang:
        print(y ,end="")
        print(" ")
        
    else:
        print(z ,end="")
        print(" ")

    
        

print("Pertandingan selesai")
if poin_x > poin_y:
    print("Klub yang memenangkan pertandingan :" ,x )
elif poin_x > poin_y:
    print("Klub yang memenangkan pertandingan :" ,y)

    