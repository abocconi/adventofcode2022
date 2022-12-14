
def priority_get(rucksack : str):
    rucksack  = rucksack.rstrip()    
    s1 = set(rucksack[0:int(len(rucksack)/2)])    
    s2 = set(rucksack[int(len(rucksack)/2):])
    retval = sum((ord(c) + 1 - ord('a')) for c in s1.intersection(s2) if ord(c) >= ord('a'))
    retval += sum((ord(c) + 27 - ord('A')) for c in s1.intersection(s2) if ord(c) < ord('a'))
    print(s1.intersection(s2), retval)
    return retval


with open("input.txt") as f:
    total = sum(priority_get(line) for line in f.readlines())
    
print(total)
    
    