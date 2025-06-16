def get_most_common_letter(text):
    counter = {}  # Counter is an empty dictionary, where we'll store the count of each character 
    for char in text:
        if char.isalpha():
            char = char.lower()
            counter[char] = counter.get(char, 0) + 1 # How many times it appears in something 
    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[0][0]
    print(f"Letter: {letter}")
    return letter

print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")


''' Actual:   [('s', 1), ('n', 1), ('!', 1), (',', 2), ('i', 2), ('t', 3), ('h', 3), ('e', 4), ('r', 4), ('f', 4), ('o', 7)] '''
# It's counting the spaces, which have more than o's 
# First we need to not count the spaces to get a more accurate list