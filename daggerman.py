import random
import map

exp = 0
lvl = 1
max_hp = 10
hp = 10
weapon = "dagger"
weapon_damage = 2
extra_damage = 0
armor = "Nothing"
armor_defense = 0
extra_defense = 0
extra_slot = "Nothing"

board_dict = {}

def roll(num_sides):
    roll = random.randint(1, num_sides)
    return roll

def board_dict_update():
    global board_dict
    for n in range (len(map.id)):
        board_dict[(map.x[n], map.y[n])] = map.id[n]

def create_square(x_coord, y_coord, identifier):
    map.x.append(x_coord)
    map.y.append(y_coord)
    map.id.append(identifier)
    map.standon.append(False)

def show_board():
    k = map.id.index("x")
    board_dict_update()
    for i in range(-3, 4):
        for j in range(-3, 4):
            cell = board_dict.get((map.x[k]+j, map.y[k]+i), " ")
            print(cell, end=" ")
        print()

def move(dx, dy):
    global action_taken
    k = map.id.index("x")
    board_dict_update()
    if board_dict.get((map.x[k]+dx, map.y[k]+dy), " ") == "□":
        map.id[k] = "□"
        map.id[next(i for i, (xx, yy) in enumerate(zip(map.x, map.y)) if xx == map.x[k]+dx and yy == map.y[k]+dy)] = "x"
        k = map.id.index("x")
        if map.standon[k] == False:
            gen()
            map.standon[k] = True
        action_taken = True

def move_object(dx,dy):
    global board_dict, m, moved
    if board_dict.get((map.x[map.MplaceID[m]]+dx, map.y[map.MplaceID[m]]+dy), " ") == "□":
        moved = True
        map.id[map.MplaceID[m]] = "□"
        map.id[next(i for i, (xx, yy) in enumerate(zip(map.x, map.y)) if xx == map.x[map.MplaceID[m]]+dx and yy == map.y[map.MplaceID[m]]+dy)] = map.Mid[m]
        map.MplaceID[m] = next(i for i, (xx, yy) in enumerate(zip(map.x, map.y)) if xx == map.x[map.MplaceID[m]]+dx and yy == map.y[map.MplaceID[m]]+dy)  
        return True  

def place_object(identifier):
    k = map.id.index("x")
    board_dict_update()
    while True:
        n = roll(4)
        if n == 1 and board_dict.get((map.x[k]-1, map.y[k]), " ") == " ":
            create_square(map.x[k]-1, map.y[k], identifier)
            return
        elif n == 2 and board_dict.get((map.x[k]+1, map.y[k]), " ") == " ":
            create_square(map.x[k]+1, map.y[k], identifier)
            return
        elif n == 3 and board_dict.get((map.x[k], map.y[k]-1), " ") == " ":
            create_square(map.x[k], map.y[k]-1, identifier)
            return
        elif n == 4 and board_dict.get((map.x[k], map.y[k]+1), " ") == " ":
            create_square(map.x[k], map.y[k]+1, identifier)
            return

def gen():
    k = map.id.index("x")
    board_dict_update()
    if board_dict.get((map.x[k]-1, map.y[k]), " ") != " " and board_dict.get((map.x[k]+1, map.y[k]), " ") != " " and board_dict.get((map.x[k], map.y[k]-1), " ") != " " and board_dict.get((map.x[k], map.y[k]+1), " ") != " ":
        return
    n = roll(30)
    if n <= 20:
        place_object("□")
    elif n <= 22:
        place_object("□")
        if board_dict.get((map.x[k]-1, map.y[k]), " ") != " " and board_dict.get((map.x[k]+1, map.y[k]), " ") != " " and board_dict.get((map.x[k], map.y[k]-1), " ") != " " and board_dict.get((map.x[k], map.y[k]+1), " ") != " ":
            return
        place_object("□")
    elif lvl == 1:
        if n <= 25:
            place_object("S")
            map.Mhp.append(2)
            map.Mdamage.append(3)
            map.Mdefense.append(0)
            map.Mexp.append(1)
            map.Mid.append("S")
            map.MplaceID.append(len(map.id)-1)
        elif n <= 28:
            place_object("K")
            map.Mhp.append(4)
            map.Mdamage.append(2)
            map.Mdefense.append(0)
            map.Mexp.append(2)
            map.Mid.append("K")
            map.MplaceID.append(len(map.id)-1)
        else:
            place_object("C")
    elif lvl == 2:
        if n <= 24:
            place_object("K")
            map.Mhp.append(4)
            map.Mdamage.append(2)
            map.Mdefense.append(0)
            map.Mexp.append(2)
            map.Mid.append("K")
            map.MplaceID.append(len(map.id)-1)
        elif n <= 26:
            place_object("L")
            map.Mhp.append(10)
            map.Mdamage.append(4)
            map.Mdefense.append(1)
            map.Mexp.append(4)
            map.Mid.append("L")
            map.MplaceID.append(len(map.id)-1)
        elif n <= 28:
            place_object("F")
            map.Mhp.append(6)
            map.Mdamage.append(6)
            map.Mdefense.append(0)
            map.Mexp.append(3)
            map.Mid.append("F")
            map.MplaceID.append(len(map.id)-1)
        else:
            place_object("C")
    elif lvl >= 3:
        if n <= 24:
            place_object("F")
            map.Mhp.append(6)
            map.Mdamage.append(6)
            map.Mdefense.append(0)
            map.Mexp.append(3)
            map.Mid.append("F")
            map.MplaceID.append(len(map.id)-1)
        elif n <= 26:
            place_object("O")
            map.Mhp.append(10)
            map.Mdamage.append(8)
            map.Mdefense.append(2)
            map.Mexp.append(6)
            map.Mid.append("O")
            map.MplaceID.append(len(map.id)-1)
        elif n <= 28:
            place_object("T")
            map.Mhp.append(16)
            map.Mdamage.append(6)
            map.Mdefense.append(3)
            map.Mexp.append(7)
            map.Mid.append("T")
            map.MplaceID.append(len(map.id)-1)
        else:
            place_object("C")

def equip():
    print("Do you want to equip this item? (y/n)")
    choice = input()
    return choice

def attack(dx, dy):
    global action_taken, weapon, weapon_damage, armor, armor_defense, extra_slot, extra_damage, extra_defense, exp, lvl, max_hp, hp
    k = map.id.index("x")
    target_x = map.x[k] + dx
    target_y = map.y[k] + dy
    for n in range(len(map.id)):
        if map.x[n] == target_x and map.y[n] == target_y:
            if map.id[n] == "C":
                action_taken = True
                print("You open the chest and find treasure!")
                map.id[n] = "□"
                if lvl == 1:
                    treasure_roll = roll(4)
                    if treasure_roll == 1:
                        print("You found a dagger! (Damage 1d3)")
                        if equip() == "y":
                            weapon = "dagger"
                            weapon_damage = 3
                    elif treasure_roll == 2:
                        print("You found a Leather Armor! (Defense +1)")
                        if equip() == "y":
                            armor = "Leather Armor"
                            armor_defense = 1
                    elif treasure_roll == 3:
                        print("You found a attack ring! (Damage +1)")
                        if equip() == "y":
                            extra_slot = "attack ring 1"
                            extra_damage = 1
                            extra_defense = 0
                    elif treasure_roll == 4:
                        print ("You found a a defense amulet! (Defense +1)")
                        if equip() == "y":
                            extra_slot = "defense amulet 1"
                            extra_defense = 1
                            extra_damage = 0
                if lvl == 2:
                    treasure_roll = roll(6)
                    if treasure_roll == 1:
                        print("You found a short sword! (Damage 1d6)")
                        if equip() == "y":
                            weapon = "short sword"
                            weapon_damage = 6
                    elif treasure_roll == 2:
                        print("You found a Chainmail Armor! (Defense +2)")
                        if equip() == "y":
                            armor = "Chainmail Armor"
                            armor_defense = 2
                    elif treasure_roll == 3:
                        print("You found a swift dagger! (Damage 1d4, use q for swift attack)")
                        if equip() == "y":
                            weapon = "swift dagger"
                            weapon_damage = 4
                    elif treasure_roll == 4:
                        print("You found a power ring! (Damage, defense +1)")
                        if equip() == "y":
                            extra_slot = "power ring 1"
                            extra_damage = 1
                            extra_defense = 1
                    elif treasure_roll == 5:
                        print ("You found a heal magic scroll! (heal 2 hp when casted)")
                        if equip() == "y":
                            extra_slot = "heal 2 magic scroll"
                            extra_defense = 0
                            extra_damage = 0
                    elif treasure_roll == 6:
                        print ("You found a health potion! (Restores hp to max when used)")
                        if equip() == "y":
                            extra_slot = "health potion"
                            extra_damage = 0
                            extra_defense = 0
                if lvl >= 3:
                    treasure_roll = roll(6)
                    if treasure_roll == 1:
                        print("You found a longsword! (Damage 1d8)")
                        if equip() == "y":
                            weapon = "longsword"
                            weapon_damage = 8
                    elif treasure_roll == 2:
                        print("You found a chainmail armor! (Defense +2)")
                        if equip() == "y":
                            armor = "chainmail armor"
                            armor_defense = 2
                    elif treasure_roll == 3:
                        print("You found a swift dagger! (Damage 1d6, use q for swift attack)")
                        if equip() == "y":
                            weapon = "swift dagger"
                            weapon_damage = 6
                    elif treasure_roll == 4:
                        print("You found a attack ring! (Damage +2)")
                        if equip() == "y":
                            extra_slot = "attack ring 2"
                            extra_damage = 2
                            extra_defense = 0
                    elif treasure_roll == 5:
                        print ("You found a a defense amulet! (Defense +2)")
                        if equip() == "y":
                            extra_slot = "defense amulet 2"
                            extra_defense = 2
                            extra_damage = 0
                    elif treasure_roll == 6:
                        print ("You found a health potion! (Restores hp to max when used)")
                        if equip() == "y":
                            extra_slot = "health potion"
                            extra_damage = 0
                            extra_defense = 0
            elif map.id[n] != "□":
                action_taken = True
                print(f"You attack the {map.id[n]}!")
                monster_index = map.MplaceID.index(n)
                attack_roll = roll(weapon_damage) + extra_damage - map.Mdefense[monster_index]
                if attack_roll <= 0:
                    print("Your attack did no damage!")
                    return
                print(f"You deal {attack_roll} damage!")
                map.Mhp[monster_index] -= attack_roll
                if map.Mhp[monster_index] <= 0:
                    print(f"You defeated the {map.id[n]}!")
                    exp_gain = map.Mexp[monster_index]
                    print(f"You gain {exp_gain} EXP!")
                    exp += exp_gain
                    map.id[n] = "□"
                    map.Mhp.pop(monster_index)
                    map.Mdamage.pop(monster_index)
                    map.Mdefense.pop(monster_index)
                    map.Mexp.pop(monster_index)
                    map.Mid.pop(monster_index)
                    map.MplaceID.pop(monster_index)
                    if exp >= lvl * 10:
                        exp -= lvl * 10
                        lvl += 1
                        print(f"You leveled up! You are now level {lvl}!")
                        max_hp += 5
                        hp = max_hp
                        print(f"Your max HP increased to {max_hp}!")
            else:
                return

map.x.append(0)
map.y.append(0)
map.id.append("x")
map.standon.append(True)
create_square(1, 0, "□")
create_square(-1, 0, "□")

print ("You are 'x'.")
print ("Squares you can stand on are marked with '□'.")
print ("After we ask you for your action you can type w a s or d to move.")
print ("Or you can type ww aa ss or dd to attack in that direction.")
print ("you can also type i to see your inventory and statts.")
print ("You can type m to see every monster that you can currently fight.")
print ("You can type quit to end the game.")
print ("if you want the instructions again type h.")
print ("Later you may get more options.")
print ("You can open chests by attacking them.")
print ("Good luck!")

heal = 0
while True:
    action_taken = False
    print()
    show_board()
    print()
    print("choose an action: ")
    action = input()
    if action == "i":
        print(f"HP: {hp}/{max_hp}, EXP: {exp}, Level: {lvl}, Exp to next level: {lvl * 10- exp}")
        print(f"Weapon: {weapon} (Damage: 1d{weapon_damage})")
        print(f"Armor: {armor} (Defense: {armor_defense})")
        print(f"Extra Slot: {extra_slot}")
        print()
    elif action == "quit":
        break
    elif action == "a":
        move(-1, 0)
    elif action == "d":
        move(1, 0)
    elif action == "w":
        move(0, -1)
    elif action == "s":
        move(0, 1)
    elif action == "h":
        print ("w a s or d to move.")
        print ("aa ss dd or ww to attack in that direction.")
        print ("i - see your inventory and statts.")
        print ("m - see monsters you can fight.")
        if extra_slot == "health potion":
            print ("r - restore hp to max.")
        if weapon == "swift dagger":
            print ("q - swift attack.")
        if extra_slot[-12:-1] == "magic scroll":
            print ("e - cast spell.")
        print ("quit - end the game.")
        print ("h - see this help message again.")
        print ("Later you may get more options.")
        print ("You can open chests by attacking them.")
        print ("Good luck!")
    elif action == "m":
        print("level 1 monsters:")
        print("K - Kobold (HP: 4, Damage: 1d2)")
        print("S - slime (HP: 2, Damage: 1d3) slimes can't move")
        if lvl >= 2:
            print("level 2 monsters:")
            print("L - Lizardman (HP: 10, Damage: 1d3, defense: 1)")
            print("F - Freakish Abberation (HP: 6, Damage: 1d6)")
            if lvl >= 3:
                print("level 3 monsters:")
                print("O - Orc (HP: 10, Damage: 1d8, defense: 2)")
                print("T - Troll (HP: 16, Damage: 1d6, defense: 3)")
    elif action == "aa":
        attack(-1, 0)
    elif action == "dd":
        attack(1, 0)
    elif action == "ww":
        attack(0, -1)
    elif action == "ss":
        attack(0, 1)
    elif action == "r":
        if extra_slot == "health potion":
            hp = max_hp
            print("You used the health potion and restored your HP to max!")
            extra_slot = "Nothing"
            action_taken = True
    elif action == "q":
        if weapon == "swift dagger":
            attack(0, -1)
            attack(-1, 0)
            attack(1, 0)
            attack(0, 1)
    elif action == "e":
        if extra_slot == "heal 2 magic scroll":
            hp += 2
            if hp > max_hp:
                hp = max_hp
            print("You cast the heal spell and restored 2 HP!")
            action_taken = True
    if action_taken:
        k = map.id.index("x")
        for m in range(len(map.Mid)):
            if abs(map.x[map.MplaceID[m]]-map.x[k]) + abs(map.y[map.MplaceID[m]]-map.y[k]) <= 1:
                print(f"The {map.Mid[m]} attacks you!")
                monster_attack = roll(map.Mdamage[m]) - (armor_defense + extra_defense)
                if monster_attack <= 0:
                    print("The monster's attack did no damage!")
                    continue
                print(f"The {map.Mid[m]} deals {monster_attack} damage!")
                hp -= monster_attack
                print (f"Your HP is now {hp}/{max_hp}.")
                if hp <= 0:
                    print("GAME OVER")
                    exit()
            elif map.Mid[m] == "S":
                continue
            else:
                board_dict_update()
                if board_dict.get((map.x[k]-1, map.y[k]), " ") != "□" and board_dict.get((map.x[k]+1, map.y[k]), " ") != "□" and board_dict.get((map.x[k], map.y[k]-1), " ") != "□" and board_dict.get((map.x[k], map.y[k]+1), " ") != "□":
                    continue
                moved = False
                while moved == False:
                    roll_dir = roll(4)
                    if roll_dir == 1:
                        move_object(-1, 0)
                    elif roll_dir == 2:
                        move_object(1, 0)
                    elif roll_dir == 3:
                        move_object(0, -1)
                    elif roll_dir == 4:
                        move_object(0, 1)
        if heal == 0:
            heal = 1
        else:
            if hp < max_hp:
                hp += 1
            heal = 0
                