import random

""" DECLARATIONS """
answers = {}
questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? "
}
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

""" FUNCTIONS """
def pirateDrinks():
    """ Call functions in order needed. """
    askQuestions()
    createDrink(answers, ingredients)

def askQuestions():
    """ Itterate over each question in the questions dictionary. Each response will be added to the the answers dictionary. """
    print "Answer each question to determine your drink of the night. Use 'y' or 'n' as your response."
    for k,v in questions.items():
        reply = raw_input(v).lower()
        if reply == "y":
            answers[k] = True
        else:
            answers[k] = False
    return answers

def createDrink(answers, ingredients):
    """ Create the drink based on the answers given by matching answers and selecting a random matching ingredient. """
    print "\nHere's your drink!"
    for k,v in answers.items():
        if v == True:
            print "{0}".format(ingredients[k][random.randint(0, 2)])
    return

""" Instructions:
The function should ask each of the questions in the questions dictionary, and gather the responses in a new dictionary.
The new dictionary should contain the type of ingredient (for example "salty", or "sweet"), mapped to a Boolean value.
If the customer answers y or yes to the question then the value should be True, otherwise the value should be False.
The function should return the new dictionary.

Remember that you can use the raw_input function to get an answer from the customer. """

if __name__ == '__main__':
    pirateDrinks()
