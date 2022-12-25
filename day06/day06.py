
with open("input.txt") as f:
    stream = f.read()    

#part 1    
index = 0
while len(set(stream[index:index+4])) != 4:
    index += 1

print(stream[index:index+4], index+4)

#part 2
index = 0
while len(set(stream[index:index+14])) != 14:
    index += 1

print(stream[index:index+14], index+14)

