import options

classes = options.classes()


for id, clas in enumerate(classes): 
    print (f'{id+1}) {clas}')

choice = input("select a number")

print(classes[int(choice)-1])