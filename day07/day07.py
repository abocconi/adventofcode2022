class TreeNode:
    
    def __init__(self, name : str, parent : 'TreeNode' = None):
        self.name = name
        self.parent = parent
        self.children = []
        self.localsize = 0          

class CLParser:
    
    def __init__(self):   
        self.root = TreeNode("*")     
        self.currentDir = self.root        
        
    def __newdir(self, dirName: str):
        #print("directory: ", dirName)
        newdir = TreeNode(dirName, self.currentDir)
        self.currentDir.children.append(newdir)
        return

    def __addfile(self, filename : str, filelenght : int):
        #print("file: ", filename, "of size", filelenght)    
        self.currentDir.localsize += filelenght
        return
        
    def __cmd(self, args : list[str]):
        if args[0].startswith("cd"):
            if args[1].startswith("/"):
                #print("root")
                self.currentDir = self.root            
            elif args[1].startswith(".."):            
                #print("back")
                if self.currentDir.parent:
                    self.currentDir = self.currentDir.parent
            else:
                #print("entering ", args[1])
                for child in self.currentDir.children:
                    if child.name == args[1]:
                        self.currentDir = child
                        break

        elif args[0].startswith("ls"):                       
            pass
        
        #print(self.currentDir.data)        
        return

    def __getTotals(self, root : TreeNode, totals):        

        if root is None:
            return
        
        totalSize = root.localsize
        
        for child in root.children:            
            totalSize += self.__getTotals(child, totals)            

        totals.append(totalSize)
        return totalSize

    def totals(self):
        totals = []
        self.__getTotals(self.root, totals)
        return totals
    
    def totalBelow100000(self):                
        return sum(size for size in self.totals() if size < 100000)

    def totalSize(self):                
        return max(self.totals())
    
    def smallestDirectoryAbove(self, minsize):
        return min(list(filter(lambda size: size >= minsize, self.totals())))

    def parse(self, line):
        
        if line[0].startswith('$'):
            self.__cmd(line[1:])
        elif line[0].startswith('dir'):
            self.__newdir(line[1])      
        elif line[0].isdecimal():
            self.__addfile(line[1], int(line[0]))



parser = CLParser()

with open("input.txt") as f:
    for line in f.readlines():
        parser.parse(line.split())
 
# part 1
print(parser.totalBelow100000())       

# part 2
print(parser.smallestDirectoryAbove(30000000-(70000000-parser.totalSize())))

