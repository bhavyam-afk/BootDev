def analytics1(content):
    words = content.split()
    return len(words)

def characterCount(content):
    char_counts = {}

    for character in content:
        character = character.lower()

        if character in char_counts:
            char_counts[character] += 1
        else:
            char_counts[character] = 1
    return char_counts

def sortedChars(char_map):
    results = []

    for ch, count in char_map.items():
        if ch.isalpha():
            results.append({
                "char": ch,
                "num": count
            })
    results.sort(reverse=True, key=lambda x: x["num"])
    return results

