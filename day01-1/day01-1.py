
calories = []
with open('input.txt') as f:
    for line in f.read().split('\n\n'):
        calories.append(sum(int(x) for x in line.rstrip('\n').split('\n')))    
print(max(calories))


        





        




        

        



        


                    
        
        
    


                                   
       

        



