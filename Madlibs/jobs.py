def madlib():
    occupation1 = ("Occupation (a job): ")
    noun1 = input("Noun: ")
    adj1 = input("Adjective: ")
    noun2 = input("Noun: ")
    verb1 = input("Verb: ")
    adj2 = input("Adjective: ")
    noun3 = input("Noun: ")
    verb2 = input("Verb: ")
    noun4 = input("Noun: ")
    verb3 = input("Verb: ")
    
    madlib = f"Today a {occupation1} named {noun4} came to our school \
to talk to us about her job. She said the most important skill you \
need to know to do her job is to be able to {verb2} around (a) {adj1} {noun3}. \
She said it was easy for her to learn her job because she loved to {verb1} when \
she was my age--and that helps a lot! If you're considering her profession, I hope \
you can be near (a) {adj2} {noun1}. That's very important! If you get too distracted \
in that situation you won't be able to {verb3} next to (a) {noun2}!"

    print(madlib)