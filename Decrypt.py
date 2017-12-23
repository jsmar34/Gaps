# Decryption of Gaps

inPUT = input("Paste the number sequence line by line: ")
output = []
output2 = []
output3 = []
output4 = []

# List sets

aToG = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

hToP = ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

qToS = ['q', 'r', 's']

tToV = ['t', 'u', 'v']

wToX = ['w', 'x']

yToZ = ['y', 'z']

groups = [aToG, hToP, qToS, tToV, wToX, yToZ]

for char in inPUT:
    output.append(char)


output2.append(output[3])

for char in output:
    if char.isdigit() == 0:
        output.remove(char)
    else:
        output2.append(char)

for i in range(len(output2)):
    if i % 2 == 0:
        x = (int(output2[i]), int(output2[i+1]))
        output3.append(x)


for letter in output3:
    if letter[0] == 1:
        for char in aToG:
            if letter[1] == aToG.index(char) + 1:
                output4.append(char)
    elif letter[0] == 2:
        for char in hToP:
            if letter[1] == hToP.index(char) + 1:
                output4.append(char)
    elif letter[0] == 3:
        for char in qToS:
            if letter[1] == qToS.index(char) + 1:
                output4.append(char)
    elif letter[0] == 4:
        for char in tToV:
            if letter[1] == tToV.index(char) + 1:
                output4.append(char)
    elif letter[0] == 5:
        for char in wToX:
            if letter[1] == wToX.index(char) + 1:
                output4.append(char)
    elif letter[0] == 6:
        for char in yToZ:
            if letter[1] == yToZ.index(char) + 1:
                output4.append(char)


print(output3)
print(output4)

print("")
e = input("Press close to exit")
