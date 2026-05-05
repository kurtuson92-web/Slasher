# player
hero_hp = 150
hero_attack = 20
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
    "Cannon Ball": {"price": 20, "attack": 3},
    "Heavy Ball": {"price": 75, "attack": 10},
    "Med Kit":{"price":25,"hp":10}
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
    print("4. Run")

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

        item_list = list(sample_items.items())

        for i, (item, data) in enumerate(item_list, start=1):
            print(f"{i}. {item} - {data['price']} gold")

        print("0. Exit")

        choice = input("Choose item number: ")

        if choice == "0":
            print("Thanks for Buying!!")
            print("Leaving shop...")

        elif choice.isdigit():
            index = int(choice) - 1

            if 0 <= index < len(item_list):
                item_name, item_data = item_list[index]

                if hero_gold >= item_data["price"]:
                    hero_gold -= item_data["price"]
                    inventory.append(item_name)

                    if "attack" in item_data:
                        hero_attack += item_data["attack"]

                    if "hp" in item_data:
                        hero_hp += item_data["hp"]

                    print(f"You bought {item_name}!")
                else:
                    print("Not enough gold!")
            else:
                print("Invalid choice.")
        else:
            print("Enter a number only.")

    # RUN
    elif action == "4":
        print("You ran away!")
        break

    else:
        print("Please Choose Valid Choice")

