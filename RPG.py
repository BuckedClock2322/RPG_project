#imports the random func
import random
#imports sleep func
from time import sleep
#locations dictionary/index. 
#The dictionary shows the title, description, items, exits, enemies and what items are needed
locations = { 
    0: {
        "title": "Bus Station",
        "description": "An empty bus station. The next bus is due in an hour.\nYou consider calling a taxi but decide not to.",
        "items": [],
        "requires": False,
        "exits": {
            "north": 1,
            "west": 4,
        }
    },
    1: {
        "title": "Underground Walkway",
        "description": "Walkway under the A41.\n You can smell how long it has been since the council has cleaned the walls.",
        "items": [],
        "requires": False,
        "exits": {
            "south": 0,
            "north": 2,
            "east": 3,
        }
    },
    2: {
        "title": "Supermarket",
        "description": "You are outside of a closed Tesco express. You see a shady looking person hanging around the corner.",
        "items": ["baggie"],
        "requires": "cash",
        "exits": {
            "south": 1,
        }
    },
    3: {
        "title": "Multi-storey Carpark",
        "description": "A closed carpark.\n You see a car with a broken window.",
        "items": ["cash"],
        "requires": False,
        "exits": {
            "west": 1
        }
    },
    4: {
        "title": "Alleyway",
        "description": "Dimly lit alleyway. There is a person in the shadows asking for a baggie to go away.",
        "items": [],
        "requires": "baggie",
        "exits": {
            "south": 5,
            "east": 0,
            "west": 6
        }
    },
    5: {
        "title": "Main Street",
        "description": "Decrepit Main Street. Shops are all closed, except for the Betfred",
        "items": [],
        "requires": False,
        "exits": {
            "north east": 9,
            "north": 4,
            "east": 8,
        }
    },
    6: {
        "title": "Police Checkpoint",
        "description": "Police Checkpoint. They are looking for suspects and evidence. \n You hate being an intern for them",
        "items": ["train ticket"],
        "requires": "evidence",
        "exits": {
            "south": 7,
            "east": 4,
        }
    },
    7: {
        "title": "Train Station",
        "description": "Train Station with a daily journey to Manchester and beyond. \n AKA your way out.",
        "items": [],
        "requires": "train ticket",
        "exits": {
            "north": 6,
        }
    },
    8: {
        "title": "Pub",
        "description": "Average Spoons, you might have suspects hanging out behind.",
        "items": [],
        "requires": False,
        "exits": {
            "west": 5,
            "north": 9,
        }
    },
    9: {
        "title": "Behind Pub",
        "description": "You can see the back of the pub, and a few people are hanging out.",
        "items": ["evidence"],
        "enemies": ["Barry,63"],
        "requires": False,
        "exits": {
            "south": 8,
            "south west": 5,
        }
    },
}

#player config
player = {
    #starts the player off in the first location which is the bus station
    "location": 0,
    #starts the player off with no items
    "items": [],
    #player starts with 100 health
    "health":100,
    #player starts with 10 health
    "player_damage": random.randint(1,10),
}

#display location function
def display_location(loc):
    #prints a placeholder to clearly show the location
    print("\n+-----------------------------------------+")
    #prints the location title
    print(loc["title"])
    #prints the location description
    print(loc["description"])
    #prints the location exits on a new line
    print("\nExits:")
    for direction, index in loc["exits"].items():
        print(f"{direction.capitalize()} - {locations[index]['title']}")

#view location+items function
def view_items(loc):
    if loc["items"]:
        #tells the user what items there are
        print("\nYou see:")
        for item in loc["items"]:
            print(f"  {item}")

#view player's items function
def view_player(items):
    print(f" Player Health: {player["health"]}")
    if items:
        #tells the user what items they have
        print("\nYou are holding:")
        for item in items:
            #prints the items you have
            print(f"  {item}")
    else:
        #tells the user that they have no items
        print("\nYou are not holding anything.")

#enemies index
enemies = {
    "Barry,63": {"health": 50, "attack": 10,
    }, 
}

# Function to handle combat with an enemy
def attack_enemy(enemy):
    global player
    player_damage = random.randint(1,10)
    enemy_damage = random.randint(1,10)

    #attacks the enemy
    print(f"\nYou attack {enemy} for {player_damage} damage!")
    #takes damage from enemy health
    enemies["Barry,63"]["health"] -= player_damage
    #if the enemy health goes under 0, the enemy is defeated
    if enemies["Barry,63"]["health"] <= 0:
        print(f"{enemy} is defeated!")
        return

    # Enemy attacks back
    print(f"{enemy} attacks you for {enemy_damage} damage!")
    #enemy damage is taken off player health
    player["health"] -= enemy_damage
    #if player health goes under 0, player is defeated and the game ends
    if player["health"] <= 0:
        print("You have been defeated... Game Over!")
        exit()

# Function to display enemies in the location
def view_enemies(loc):
    if "enemies" in loc:
        print("\nEnemies present:")
        for enemy in loc["enemies"]:
            print(f"  {enemy} - Health: {enemies[enemy]['health']}")

#end game function
def ending():
    #if the player is at the train station and has a train ticket, the game ends
    if player["location"] == 7 and "train ticket" in player["items"]:
        print("Well Done! You have finished the game. \n You catch a train home and go to sleep.")
        print("Did you expect a masssive game with a good story? \n This was fueled by Monster Energy and lack of sleep. \n Game's over. Go home!")
        print("Thank you for playing!")
        exit()

#The game function
def game(): 
    message = ""
    # Starts a loop
    while True:
        # The location where the player is added to the current location index
        current_location_index = player["location"]
        loc = locations[current_location_index]

        # Display location and player status
        display_location(loc)
        # Display items at the location
        view_items(loc)
        # Display the player's items
        view_player(player["items"])
        # Display enemies at the location
        view_enemies(loc)
        #end game function
        ending()
        if message:
            print(f"\n{message}")
            message = ""

        # Get user action
        action = input("> ").strip().lower()

        # Handle attacking
        if action == "attack":
            #check for enemies
            if "enemies" in loc and loc["enemies"]:
                #retrives the first enemy in the list
                enemy = loc["enemies"][0]
                #passes the enemy to the attack function
                attack_enemy(enemy)  

                # If the enemy is defeated, remove them
                if enemies[enemy]["health"] <= 0:
                    print(f"{enemy} is no longer a threat.")
                    loc["enemies"].remove(enemy)
            else:
                message = "There are no enemies here to attack."

        # Exits the game
        elif action == "exit":
            print("Exiting Program...")
            sleep(2)
            print("Goodbye.")
            break

        # Handles movement
        elif action in loc["exits"]:
            next_location_index = loc["exits"][action]
            next_location = locations[next_location_index]

            # Checks if the next location requires an item
            if next_location["requires"]:
                if next_location["requires"] in player["items"]:
                    player["location"] = next_location_index
                    message = f"You used the {next_location['requires']} to enter."
                else:
                    message = f"You need {next_location['requires']} to go there!"
            else:
                player["location"] = next_location_index

        # Handles taking items
        elif action.startswith("take "):
            item = action[5:]
            if item in loc["items"]:
                loc["items"].remove(item)
                player["items"].append(item)
                message = f"You took the {item}."
            else:
                message = f"There is no {item} here."

        # Handles dropping items
        elif action.startswith("drop "):
            item = action[5:]
            if item in player["items"]:
                player["items"].remove(item)
                loc["items"].append(item)
                message = f"You dropped the {item}."
            else:
                message = f"You don't have {item} to drop."
        else:
            message = "I don't understand that command."


game()