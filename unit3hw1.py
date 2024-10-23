age_in_months = int(input("how old in months is the cat?"))

def cat_approach1(age_in_months):
    if age_in_months <= 6:
        print(f"Category: Kitten, Price: $250")
    elif 7 <= age_in_months <= 11:
        print(f"Category: Teenager, Price: $225")
    elif 12 <= age_in_months <= 95:
        print(f"Category: Adult, Price: $150")
    elif age_in_months >= 96:
        print(f"Category: Senior, Price: $85")

def cat_approach2(age_in_months):
    if age_in_months >= 96:
        print(f"Category: Senior, Price: $85")
    elif 12 <= age_in_months <= 95:
        print(f"Category: Adult, Price: $150")
    elif 7 <= age_in_months <= 11:
        print(f"Category: Teenager, Price: $225")
    elif age_in_months <= 6:
        print(f"Category: Kitten, Price: $250")

def cat_approach3(age_in_months):
    if age_in_months <= 6:
        print(f"Category: Kitten, Price: $250")
    if 7 <= age_in_months <= 11:
        print(f"Category: Teenager, Price: $225")
    if 12 <= age_in_months <= 95:
        print(f"Category: Adult, Price: $150")
    if age_in_months >= 96:
        print(f"Category: Senior, Price: $85")

def cat_approach4(age_in_months):
    if age_in_months >= 96:
        print(f"Category: Senior, Price: $85")
    if 12 <= age_in_months <= 95:
        print(f"Category: Adult, Price: $150")
    if 7 <= age_in_months <= 11:
        print(f"Category: Teenager, Price: $225")
    if age_in_months <= 6:
        print(f"Category: Kitten, Price: $250")



cat_approach1(age_in_months)
cat_approach2(age_in_months)
cat_approach3(age_in_months)
cat_approach4(age_in_months)
