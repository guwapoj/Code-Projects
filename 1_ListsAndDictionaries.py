#Ooremide Adegbola
#Comp163 section 2
#3/22/24
#Will be creating a program that will store roster and rating information for a soccer
#team. 

#Function Menu for user input
def printMenu():
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")


 #input user to add players 
def addPlayer(roster):
    jersey_number = int(input("Enter a new player's jersey number: "))
    player_rating = int(input("Enter the player's rating: "))
    
    if jersey_number not in roster:
        roster[jersey_number]=player_rating
    else:
        print("Cannot add player twice")

#Function for the user to remove players
def removePlayer(roster):
    jersey_number = int(input("Enter a jersey number: "))
    if jersey_number in roster:
        del roster[jersey_number]
    else:
        print("Player not found.")

#Function to update player ratings
def updateRating(roster):
    jersey_number = int(input("Enter a jersey number: "))
    
    if jersey_number in roster:
        new_rating = int(input("Enter a new rating for player: "))
        roster[jersey_number] = new_rating
    else:
        print("Player not found in list")

#Output the player rating
def outputRating(roster):
    rating = int(input("Enter a rating: "))
    
    print("ABOVE", rating)
    
    for jersey_number, player_rating in roster.items():
        if player_rating > rating:
            print("Jersey Number: {}, Rating: {}".format(jersey_number, player_rating))



#Output the roster
def outputRoster(roster):
    print("ROSTER")
    for items in sorted(roster.keys()):
        print("Jersey number: {}, Rating: {}".format(items, roster[items]))


#Function for user input , menu options to call and output each function
def userInput():
    player_roster = {}
    for i in range(5):
        jersey_number = int(input(f"Enter player {i+1}'s jersey number : "))
        rating = int(input(f"Enter player {i+1}'s rating: "))
        player_roster[jersey_number] = rating

    while True:
        printMenu()
        choice = input("Choose an option: ")

        if choice == 'a':
            addPlayer(player_roster)
        
        elif choice == 'd':
            removePlayer(player_roster)
       
        elif choice == 'u':
            updateRating(player_roster)
        
        elif choice == 'r':
            outputRating(player_roster)
        
        elif choice == 'o':
            outputRoster(player_roster)
        
        elif choice == 'q':
            break
        else:
            print("Invalid choice")

#To call user input
if __name__ == "__main__":
    userInput()