
def cratemover9000_move(n : int, queue_from : list, queue_to : list):
    for x in range(0, n):
        queue_to.append(queue_from.pop())


def cratemover9001_move(n : int, queue_from : list, queue_to : list):
    l = len(queue_from)
    for x in range(0, n):        
        queue_to.append(queue_from.pop(l-n))


crates1 = [[*"NBDTVGZJ"], \
          [*"SRMDWPF"], \
          [*"VCRSZ"], \
          [*"RTJZPHG"], \
          [*"TCJNDZQF"], \
          [*"NVPWGSFM"], \
          [*"GCVBPQ"], \
          [*"ZBPN"], \
          [*"WPJ"]]

# shallow copy
crates2  = [list(crate) for crate in crates1]


with open("input.txt") as f:
    lines = f.readlines()
    
    for line in lines:
        if line.startswith("move"):
            moves = line.split()
            cratemover9000_move(int(moves[1]), crates1[int(moves[3])-1], crates1[int(moves[5])-1])
            cratemover9001_move(int(moves[1]), crates2[int(moves[3])-1], crates2[int(moves[5])-1])

# part 1
print (crates1)
# part 2
print (crates2)


