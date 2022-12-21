def item_priority_get(item : str):
    if item.islower():
        return ord(item) + 1 - ord('a')
    else:
        return ord(item) + 27 - ord('A')
   
def rucksack_priority_get(rucksack : str):
    rucksack  = rucksack.rstrip()
    s1 = set(rucksack[0:int(len(rucksack)/2)])
    s2 = set(rucksack[int(len(rucksack)/2):])
    return sum(item_priority_get(item) for item in s1.intersection(s2))

def group_priority_get(rucksacks : list[str]):
    s1 = set(rucksacks[0].rstrip())
    s2 = set(rucksacks[1].rstrip())
    s3 = set(rucksacks[2].rstrip())    
    return sum(item_priority_get(item) for item in s1.intersection(s2, s3))


with open("input.txt") as f:
    rucksacks = f.readlines()
    # part 1
    print("total (1):", sum(rucksack_priority_get(line) for line in rucksacks))
    # part 2
    print("total (2):", sum(group_priority_get(rucksacks[i:i+3]) for i in range(0, len(rucksacks), 3)))
    
   
    