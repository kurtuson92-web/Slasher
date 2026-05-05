# player
hero_hp = 150
hero_attack = 10
hero_gold = 0

# enemy
enemy_hp = 150
enemy_attack = 25

def attack_enemy(enemy_hp, damage):
    return enemy_hp - damage

def attack_hero(hero_hp, damage):
    return hero_hp - damage

def gold_hero(hero_gold):
    return hero_gold + 5

sample_items = {
    "Cannon Ball +3 atk ": {"price": 20, "attack": 3},
    "Heavy Ball +10 atk ": {"price": 75, "attack": 10},
    "Med Kit +5 hp":{"price":25,"hp":5}
}

inventory = []

game_title = "\033[36m"+"""
████████╗ █████╗ ███╗   ██╗██╗  ██╗    ██████╗ ██╗      █████╗ ███████╗████████╗
╚══██╔══╝██╔══██╗████╗  ██║██║ ██╔╝    ██╔══██╗██║     ██╔══██╗██╔════╝╚══██╔══╝
   ██║   ███████║██╔██╗ ██║█████╔╝     ██████╔╝██║     ███████║███████╗   ██║   
   ██║   ██╔══██║██║╚██╗██║██╔═██╗     ██╔══██╗██║     ██╔══██║╚════██║   ██║   
   ██║   ██║  ██║██║ ╚████║██║  ██╗    ██████╔╝███████╗██║  ██║███████║   ██║   
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝
"""+"\033[0m"

hp_bar = "\033[32m┃\033[m"
e_hp = "\033[31m┃\033[0m"

while True:
    print(game_title)

    print("Your HP:", hero_hp, hero_hp * hp_bar)
    print("Gold:", "\033[93m",hero_gold,"\033[0m")
    print("Enemy HP:", enemy_hp, enemy_hp * e_hp)

    print("Defeat enemy to win")
    print("Choose action")
    print("1. Attack")
    print("2. Farm")
    print("3. Shop")
    print("4. Attributes")
    print("5. Run")

    action = input("> ")

    # ATTACK
    if action == "1":
        enemy_hp = attack_enemy(enemy_hp, hero_attack)
        hero_hp = attack_hero(hero_hp, enemy_attack)

        if hero_hp <= 0:
            print("💀 You lost!")
            break

    # FARM
    elif action == "2":
        hero_gold = gold_hero(hero_gold)

        # SHOP
    elif action == "3":
        print("\n=====SHOP ITEMS=====")
        print("Gold:", "\033[93m",hero_gold,"\033[0m")

        item_list = list(sample_items.items())

        #enumerate items lists
        for i, (item, data) in enumerate(item_list, start=1):
            print(f"{i}. {item} - \033[93m{data['price']} gold\033[0m")

        print("0. Exit")

        choice = input("Choose item number: ")

        #leaving shop
        if choice == "0":
            print("Leaving shop...")

        elif choice.isdigit():
            index = int(choice) - 1

            #lenght of items in the shop
            if 0 <= index < len(item_list):
                item_name, item_data = item_list[index]

                #checks if hero_gold is greater than or equals to item price if true helo_gold will be deducted by the price
                if hero_gold >= item_data["price"]:
                    hero_gold -= item_data["price"]
                    inventory.append(item_name)

                    #if the item is attack attributes it will add to hero attack
                    if "attack" in item_data:
                        hero_attack += item_data["attack"]

                    #if the item is hp attributes item will update the hp
                    if "hp" in item_data:
                        hero_hp += item_data["hp"]

                    #if item is successfully baught 
                    print(f"You bought {item_name}!")
                else:

                    #if gold is lessthan item price
                    print("\033[31mNot enough gold!\033[0m")
            else:
                print("Invalid choice.")
        else:
            print("Enter a number only.")


    elif action == "4":
        print("Your Attack: ",hero_attack)
        print("Enemy Attack: ",enemy_attack)

    
    # takbo hanggat may lupa
    elif action == "5":
        print("You ran away!")
        break

    else:
        print("Please Choose Valid Choice")

