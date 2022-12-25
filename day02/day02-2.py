points = [
[3, 4, 8],    #  AX AY AZ
[1, 5, 9],    #  BX BY BZ
[2, 6, 7]     #  CX CY CZ
]

with open("input.txt") as f:
    calories = sum(points[ord(line[0])-ord('A')][ord(line[2])-ord('X')] for line in f.readlines())
    
print(calories)