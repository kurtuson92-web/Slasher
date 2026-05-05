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

hp_bar = "\033[32m┃\033[m"
e_hp = "\033[31m┃\033[0m"

while True:
    print("\033[36m  __       _   __      ___ __ \033[0m")
    print("\033[36m (_ ` )   /_) (_ ` )_) )_  )_)\033[0m")
    print("\033[36m.__) (__ / / .__) ( ( (__ / \ \033[0m")

    print("Your HP:", hero_hp, hero_hp * hp_bar)
    print("Gold:", hero_gold)
    print("Enemy HP:", enemy_hp, enemy_hp * e_hp)

    print("Defeat enemy to win")
    print("Choose action")
    print("1. Attack")
    print("2. Farm")
    print("3. Run")

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

    elif action == "3":
        print("Welcome to the Shop")

    # RUN
    elif action == "3":
        print("You ran away!")
        break

