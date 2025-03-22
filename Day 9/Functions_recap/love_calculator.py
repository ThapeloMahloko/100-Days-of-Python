def calculate_love_score(name1, name2):
    
    names = name1 + name2
    true_count = 0
    for letter in names:
        if letter.lower() in "true":
            true_count += 1
    
    love_count = 0
    for letter in names:
        if letter.lower() in "love":
            love_count += 1
    
    print(str(true_count) + str(love_count))
    
calculate_love_score("Kanye West", "Kim Kardashian")