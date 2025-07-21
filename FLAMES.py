def flames_game(name1, name2):
    name_1 = list(name1)
    name_2 = list(name2)

    for char in set(name_1):
        count_1 = name_1.count(char)
        count_2 = name_2.count(char)
        min_count = min(count_1, count_2)
        for _ in range(min_count):
            name_1.remove(char)
            name_2.remove(char)

    total = len(name_1) + len(name_2)
    flames = ['F', 'L', 'A', 'M', 'E', 'S']

    while len(flames) > 1:
        index = (total - 1) % len(flames)
        flames.pop(index)

    result = flames[0]
    relationship = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affection',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }
    return relationship[result]

name1 = input("Enter the name of the first person: ").lower()
name2 = input("Enter the name of the second person: ").lower()

if __name__ == "__main__":
    result = flames_game(name1, name2)
    print(f"The relationship between {name1} and {name2} is: {result}")