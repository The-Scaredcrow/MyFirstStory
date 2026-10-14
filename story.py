heroname = input ("who is the character of this story? ")
heroage = input ("how old are they? ")

print("this is the story of", heroname, "who was", heroage, "years old")
print("they had just battled for the kingdom and took a long break of 2 whole days before being summoned by the beloved rulers  of the land, who complained about a dragon and requested it slain.")
print("and of course they just had to ask", heroname,)
print("do they accept?")
choice= input ()
if choice == "yes":
    print("'As you wish my lords'" ,heroname, "says, before they set out to slay the dragon")
if choice == "no":
    print("'I refuse', the hero says and turns away. on the walk home", heroname, "is sadly struck down by a meteor,")
if choice== "no":
    print("dying a horrifically pathetic death")
if choice == "yes":
    print(heroname, "sets out on their quest to slay the dragon, but first they visit the armory and decides what to bring. They can pick from A 'bow' and arrow or a 'sword and shield'")
choice1= input()
if choice1 == "bow":
    print(heroname, "sets out with a bow on their back and arrows on their hip, going towards the direction pointed out by the rulers.")
if choice1 == "sword and shield":
    print(heroname, "sets out with a shield on their back, and a sword on their hip")
print("after a few hours they approach a bridge and see a troll guarding it with a massive stone club in hand")
if choice1== "bow":
    print("the hero has a choice, 'shoot' before it spots you, or 'talk' too it")
if choice1 == "sword and shield":
    print("the hero approaches the troll and must choose, 'attack' or 'talk'?")
choice= input()
if choice == "shoot":
    print(heroname, "decides to attack, drawing their bow and putting on an arrow")
elif choice== "attack":
    print(heroname, "decides to attack, drawing their sword and shield at the troll, who readies it's club")
elif choice== "talk":
    print(heroname, "decides to talk with the troll, who's apparently pretty nice. after a few hours it decides to come with on the hero's adventure.")
if choice== "talk":
    print("the hero has gained an ally! They both travel togheter and easily reaches the dragons cave. due to the trolls durability and strength.")
if choice== "shoot":
    print(heroname,"shoots an arrow through the neck of the troll. it falls backwards and rips the arrow out, but soon falls to bloodloss. the hero gets past the bridge")
if choice == "attack":
    print("the hero fights the troll, and takes multiple hits both to the shield and themself, but wins either way.")
    if choice == "attack" or "shoot":
        print(heroname, "goes through the forest towards the dragon, which can be heard roaring. they face many dangers, and arrive with little strength left. abandon the mission to survive?")
    choice = input() 
    if choice == "yes": 
        print("the hero abandons the mission, knowing they cant complete it either way.")
    if choice == "no":
            print("the hero moves onwards, facing the dragon in a battle that will be spoken about for centuries to come, but never returns home to hear it.")

if choice == "talk":
    print("the hero and the troll enters the cave, and soon finds a massive pile of gold and silver treasures. but the dragon is nowhere to be found...")
    print("Until they hear a fire burning behind them that is.")
    print("the two just barely manages to dodge, and the troll raises their club and strikes the dragons head, it turns out the dragon is quite small, only 10 meters including the tail.")
    if choice1 == "bow":
        print("the hero moves behind the troll and shoots an arrow, but it bounces off. after a few strikes from the troll and a few more arrows hits the eye, causing the dragon to scream in pain and lose his sight, leading to a victory.")
        print("", heroname, "and the troll, split the trasures, bringing the treasures home in cheers")
        print("Victory achived")
    if choice1== "sword and shield":
        print("the hero rushes in at the dragon, which tries to bite but is hit again by the troll, causing it to miss. the herp slices the leg and wing of the dragon, and retreats, leaving it unable to move.")
        print("but a fire begins burning in its throat, and this time it cant be interrupted. 'dodge' or 'block'?")
        choice= input()
        if choice == "dodge":
            print ("", heroname, "dodges, but the troll cant in time. they fall to the ground, dying along with the dragon. the hero returns to the city, but was it really a victory?")
        if choice== "block":
            print("",heroname, "hold their shield infront of both themself and their ally. the shield slowly turns red hot and melts away, but the troll throws its club into the dragons head last second, and it dies, leading to a victory.")
            print("", heroname, "and the troll, split the trasures, and the hero gets home in cheers")
            print()
            print()
            print()
            print("Victory achived")