import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def find_preferences():
    preferences = {}
    for style, question in questions.items():
        response = raw_input("{}(y or n) ---> ".format(question)).lower()
        if response == "y" or response == "yes":
            preferences[style] = True
        print ""
    return preferences

def make_drink(preferences):
    drink = []
    for style, choosen in preferences.iteritems():
        if choosen:
            drink.append(random.choice(ingredients[style]))
        else:
            continue
    return drink

def name_drink():
    adjective = ["Booty-shaking", "Scurvy", "Bearded", "Vengeful", "Drunken"]
    base_name = ["Salty-Dog", "Buccaneer", "Privateer", "Freebooter", "Raider", "Marauder"]
    drink_name = random.choice(adjective) + " " + random.choice(base_name)
    return drink_name

def main():
    print "Let me make you a pirate drink!\n"
    print "Arrrr! Please answer a few questions so I can determine your tastes.\n"
    preferences = find_preferences()
    new_drink = True
    while new_drink:
        drink = make_drink(preferences)
        drink_name = name_drink()
        print "Here's your drink, Matey!"
        new_drink = False
        print "I call it the %s \n" % drink_name
        print "Here's the recipie:"
        for ingredient in drink:
            print "A %s" % ingredient
        print ""
        response = raw_input("Would you like another drink, Ye Swab?(y or n) ---> ").lower()
        if response == "y":
            new_drink = True

if __name__ == "__main__":
    main()

