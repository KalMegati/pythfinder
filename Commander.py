import option_accessor as o_a

class Commander:

    def titlecard():
        print ("__________________________________________________________________")
        print ("                __  .__     _____.__            .___             ")
        print ("  ___________ _/  |_|  |___/ ____\\__| ____    __| _/___________  ")
        print ("  \\____ \\__  \\\\   __\\  |  \\   __\\|  |/    \\  / __ |/ __ \\_  __ \\ ")
        print ("  |  |_| > __ \\|  | |   Y  \\  |  |  |   |  \\/ /_/ \\  ___/|  | \\/ ")
        print ("  |   __(____  /__| |___|  /__|  |__|___|  /\\____ |\\___  >__|    ")
        print ("  |__|       \\/          \\/              \\/      \\/    \\/        ")
        print ("__________________________________________________________________")
        print ("")
        print ("Welcome to Pathfinder, a game of adventure and imagination.")
        print ("This application will help you organize basic character ideas.")
        print ("__________________________________________________________________")
        print ("")

    def present_choice():
        link = o_a.get_choice()
        print(o_a.summarizer(link))

    def confirm_choice():
        confirm = input("Enter Y(es) or N(o): ")
        return confirm

    
