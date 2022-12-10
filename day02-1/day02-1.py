points = [
[4, 8, 3],    #  AX AY AZ
[1, 5, 9],    #  BX BY BZ
[7, 2, 6]     #  CX CY CZ
]

calories = 0
with open("input.txt") as f:
    for line in f.readlines():
        calories += points[ord(line[0])-ord('A')][ord(line[2])-ord('X')]
    
print(calories)
        
    