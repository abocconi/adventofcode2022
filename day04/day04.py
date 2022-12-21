import re

def fully_contained(line :str):
    a, b, c, d = re.split('-|,', line.strip())
    s1 = set(range(int(a), int(b)+1))
    s2 = set(range(int(c), int(d)+1))       
    return s2.issubset(s1) or s1.issubset(s2)


with open("input.txt") as f:
    # part 1
    print(sum(fully_contained(line) for line in f.readlines()))
    # part 2
    
        

        