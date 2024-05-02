# Question 1 Task buggy code

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else: 
        action = "cross a river" 
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

# Question 1 Task 2

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else: 
        action = "cross a river" 
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Sometimes seeing can be misleading")
    else: 
        action = "proceed in the dark"
        print("Welcome. Descendant of Bayne")

# Question 1 Task 3 
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else: 
        action = "cross a river" 
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Sometimes seeing can be misleading")
    else: 
        action = "proceed in the dark"
        print("Welcome. Descendant of Bayne")
if place != "forest" or "cave": pass 




# Question 2 Task 1

attendees = int(input("Enter number of attendees: "))
venue= "conference room" 
if attendees < 100:
    print(venue)
else:
    venue = "large hall"
    print(venue)
    
    
    

# Question 2 Task 2

attendees = int(input("Enter number of attendees: "))
venue= "conference room" 
additional_facilites= "projector"
if attendees < 100:
    print(venue)
    print(additional_facilites)
else:
    additional_facilites = "audio system"
    venue = "large hall"
    print(venue)
    print(additional_facilites)
    
# # Question 3

vegetarian = input("Would you like vegetarian food? ")
if vegetarian == "yes":
    print("I recommend Veggie Delight Caterers")
if vegetarian == "no":
    print("I recommend Gourmet Meals Caterers")



        
    