# Gap Lists

aToG = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

hToP = ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

qToS = ['q', 'r', 's']

tToV = ['t', 'u', 'v']

wToX = ['w', 'x']

yToZ = ['y', 'z']

print("The song of the language uses claps for pause...")

# INPUT AND CONVERSION
# Input
inPUT = input("Enter your sentence: ")
inPUT = inPUT.lower()
output = []
for char in inPUT:
    output.append(char)


def addSpace():
    print(" ) ", end="")


# Conversion
for letter in output:
    if letter in aToG:
        print("( #1, ", end="")
        print(aToG.index(letter) + 1, end="")
        addSpace()
    elif letter in hToP:
        print("( #2, ", end="")
        print(hToP.index(letter) + 1, end="")
        addSpace()
    elif letter in qToS:
        print("( #3, ", end="")
        print(qToS.index(letter) + 1, end="")
        addSpace()
    elif letter in tToV:
        print("( #4, ", end="")
        print(tToV.index(letter) + 1, end="")
        addSpace()
    elif letter in wToX:
        print("( #5, ", end="")
        print(wToX.index(letter) + 1, end="")
        addSpace()
    elif letter in yToZ:
        print("( #6, ", end="")
        print(yToZ.index(letter) + 1, end="")
        addSpace()
    elif letter == " ":
        print(" ")

# Stops from exiting

print("")
e = input("Press close to exit")
