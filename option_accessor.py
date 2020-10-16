import options

backgrounds = options.backgrounds()


for id, back in enumerate(backgrounds): 
    print (f'{id+1}) {back}')

choice = input("select a number")

print(backgrounds[int(choice)-1])