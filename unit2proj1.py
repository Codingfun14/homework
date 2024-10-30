def mad_libs_game():

    print("Welcome to the Mad Libs game! Please provide the following words.")

    
    name = input("Enter a person's name: ").title()
    month = input("Enter a month: ")
    day = input("Enter a day (1-31): ")
    year = input("Enter a year: ")

    
    nouns = [input(f"Enter noun #{i+1}: ") for i in range(5)]
    verbs = [input(f"Enter verb #{i+1}: ") for i in range(5)]
    adjectives = [input(f"Enter adjective #{i+1}: ") for i in range(3)]
    adverbs = [input(f"Enter adverb #{i+1}: ") for i in range(2)]

    
    story_template = f"""
    Once upon a time, there was a {nouns[0]} who loved to {verbs[0]} with their {adjectives[0]} {nouns[1]}.
    Every {month} {day}, {name} would {verbs[1]} {adverbs[0]} while their {nouns[2]} {verbs[2]} nearby.
    One day, they found a {adjectives[1]} {nouns[3]} that could {verbs[3]} and decided to {verbs[4]} it.
    It turned out to be a {nouns[4]} which made it a {adjectives[2]} adventure, leaving everyone {adverbs[1]} amazed.
    """


    print("\nHere's your Mad Libs story!")
    print(f"{name}\n{month}/{day}/{year}")
    print(story_template)

mad_libs_game()