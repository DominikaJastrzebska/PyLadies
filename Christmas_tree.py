#Wykorzystując pętlę narysuj choinkę, do drugiej choinki dodaj bombki

for i in range(10):
    christmas_tree = (9-i)*' '+'/'*i+'\\'*i
    print(christmas_tree)



for i in range(0,10):
    christmas_tree_baubles = (10-i)*' '+'/'*i+'\\'*i
    if i == 0:
        christmas_tree_baubles = (9-i)*' '+'*'
    elif i%4 == 0:
        christmas_tree_baubles = (10-i)*' '+'/'+'*'+'/'*(i-2)+'\\'*i
    elif i%3 == 0:
        christmas_tree_baubles = (10-i)*' '+'/'*i+'\\'*(i-2)+'*'+'\\'
    print(christmas_tree_baubles)
