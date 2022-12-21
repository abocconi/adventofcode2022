import re

def get_sets(line: str):
    a, b, c, d = re.split('-|,', line.strip())
    s1 = set(range(int(a), int(b)+1))
    s2 = set(range(int(c), int(d)+1))       
    return s1, s2
    
def overlap(line: str):
    s1, s2 = get_sets(line)
    return not s2.isdisjoint(s1)

def fully_overlap(line :str):
    s1, s2 = get_sets(line)
    return s2.issubset(s1) or s1.issubset(s2)


with open("input.txt") as f:
    lines = f.readlines()        
    # part 1
    print(sum(fully_overlap(line) for line in lines))
    # part 2
    print(sum(overlap(line) for line in lines))
