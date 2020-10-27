import options

classes = options.classes()


for id, clas in enumerate(classes.keys()): 
    print (f'{id+1}) {clas}')

choice = input("select a number \n")

print(classes[list(classes.keys())[int(choice)-1]])