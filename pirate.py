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
        response = raw_input("{}(y or n) ---->".format(question)).lower()
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

def main():
    print "Let me make you a pirate drink!"
    print "Arrgg! Please answer a few questions so I can determine your tastes."
    preferences = find_preferences()
    drink = make_drink(preferences)
    print "Here's your drink, Matey!"
    print "Here's the recipie:"
    for ingredient in drink:
        print "A %s" % ingredient

if __name__ == "__main__":
    main()

