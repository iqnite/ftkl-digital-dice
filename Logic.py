'''
Digitaler Würfel Decodier-Logik
Philipp D. und Lisa K.
Apr. 2023
'''


n = False
t = True


# Eingänge

'''
1 = tnt
2 = nnn
3 = nnt
4 = ntn
5 = ntt
6 = tnn
'''

z = n  # INC
y = n  # INB
x = n  # INA


# Makros

nx = not x
ny = not y
nz = not z

nxz = not (x and z)
nnxny = not (nx and ny)

# Decode

a = not (nxz and not (nx and y))
b = not (nxz and not (nz and ny))
c = not (not (x and y) and not (nx and z))
d = not nxz
e = nnxny
f = not not (not nnxny and nz)
g = a


# Simulation

if not a:
    print("--")
else:
    print(" ")
if not b:
    print("|", end="")
else:
    print(" ", end="")
if not c:
    print("|")
else:
    print(" ")
if not d:
    print("--")
else:
    print(" ")
if not e:
    print("|", end="")
else:
    print(" ", end="")
if not f:
    print("|")
else:
    print(" ")
if not g:
    print("--")
else:
    print(" ")
