from random import randint
import os
# zadání iniciálních variables

p = 0
n = 9
a = 0
k = 0
l = 0
dil = 'd'
ero = 'e'
konec = 'q'
none = 'z'
# funkce která printuje aktuální stav gridu
def showfield(n, pole2):
    for n in range(3):
        for y in range(3):
            print(pole2[n][y], end = " ")
        print()

#pole2 = [[randint(1,10) for n in range(3)] for y in range(3)]

#print(pole2)
#showfield(n, pole2)
#print()

# funkce dilitace: pokud nejsou žádné hodnoty v parametru, zvýší všechny hodnoty v gridu o 1, pokud jsou tak zvýší hodnotu v dáné souřadnici 
def dilatace(n, pole2, b, c):
        if b == -1 and c == -1:
            for n in range(3):
                for y in range(3):
                    pole2[n][y] += 1
                    if pole2[n][y] > 10:            #tenhle if je použitý pokud nejsou žádné hodnoty v parametru zvyší všechny hodnoty v gridu o 1
                           pole2[n][y] = 10
                    print(pole2[n][y], end = " ")  
                print()
        else:
            pole2[b][c] += 1
            for n in range(3):
                for y in range(3):                  #tenhle if je použitý pokud jsou zadané hodnoty do parametru a zvýší o 1 na daných souřadnicích parametru
                    if pole2[n][y] > 10:
                         pole2[n][y] = 10
                    print(pole2[n][y], end = " ")
                print()

#dilatace(n, pole2, b, c)


# funkce eroze: pokud nejsou žádné hodnoty v parametru, sníží všechny všechny hodnoty v gridu o 1, pokud jsou tak sníší hodnotu v dáné souřadnici
def eroze(n, pole2, b, c):
        if b == -1 and c == -1:
            for n in range(3):
                for y in range(3):
                    pole2[n][y] -= 1
                    if pole2[n][y] < 1:             #tenhle if je použitý pokud nejsou žádné hodnoty v parametru zmenší všechny hodnoty v gridu o 1
                           pole2[n][y] = 1
                    print(pole2[n][y], end = " ")  
                print()
        else:
            pole2[b][c] -= 1
            for n in range(3):
                for y in range(3):
                    if pole2[n][y] < 1:             #tenhle if je použitý pokud jsou zadané hodnoty do parametru a zmenší o 1 na daných souřadnících parametru
                           pole2[n][y] = 1
                    print(pole2[n][y], end = " ")
                print()

#eroze(n, pole2, b, c)

# tohle je hlavní game loop tady se vygeneruje nový grid, ukáže nabítku možností atd.
while True:
    print()                    # mezera pro lepší čtení
    pole2 = [[randint(1,10) for n in range(3)] for y in range(3)]       # tohle vygeneruje nový grid a i ukáže
    showfield(n,pole2)                                              #/
    print()
    print("d = dilatace, e = eroze, q = konec.")        # \
    p = input()                                         #  \
    if p == konec:                                      #   \
        exit()                                          #    tahle sekce je nabítka možností co může hráč udělat a taky kde vezme input uživatele a uloží do variable
    print("x pokud žádný parametr napište 0")           #    /
    k = int(input())                                    #   /
    print("y pokud žádný parametr napište 0")           #  /
    l = int(input())                                    # /
    c = k - 1                                           # upraví číslo tak aby to začínalo od 1 do 9 (příklad chce levou horní číslici napíše 1, 1 a tohle to změní na 0, 0 což je začátek gridu)
    b = l - 1
    if p == dil:                                        # \
       dilatace(n, pole2, b, c)                         #  tahle sekce vybere podle volby uživatele dilitaci nebo erozi
    if p == ero:                                        #  /
        eroze(n, pole2, b, c)                           # /
