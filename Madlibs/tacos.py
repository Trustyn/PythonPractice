def madlib():
    adj1 = input("Adjective: ")
    foods1 = input("Foods (plural): ")
    verb1 = input("Verb: ")
    saying1 = input("Saying: ")
    noun1 = input("Noun: ")
    foods2 = input("Foods (plural): ")
    color1 = input("Color: ")
    question1 = input("Something you would ride in: ")
    animal1 = input("Animal: ")
    person1 = input("Person: ")

    madlib = f"Today I went to my favorite Taco Stand called the {adj1} {animal1}. \
Unlike most food stands, they cook and prepare the food in a {question1} \
while you {verb1}. The best thing on the menu is the {color1} {noun1}. \
Instead of ground beef they fill the taco with {foods2}, \
cheese, and top it off with a salsa made from {foods1}. \
If that doesn't make your mouth water, then it' just like {person1} \
always says: {saying1}"

    print(madlib)