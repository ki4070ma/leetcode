def minion_game(string):
    consonants_set = set([])
    vowels_set = set([])
    for i, c in enumerate(list(string)):
        for j in range(i+1, len(string)+1):
            word = string[i:j]
            if word:
                if word[0] in ['A', 'E', 'I', 'O', 'U']:
                    vowels_set.add(word)
                else:
                    consonants_set.add(word)
    consonants_score = 0
    for word in list(consonants_set):
        consonants_score += count_word(string, word)
    vowels_score = 0
    for word in list(vowels_set):
        vowels_score += count_word(string, word)
    if consonants_score > vowels_score:
        print("Stuart %d" % consonants_score)
    else:
        print("Kevin %d" % vowels_score)

def count_word(line, word):
    count = 0
    for i in range(len(line)):
        if word == line[i:i+len(word)]:
            count += 1
        if i + len(word) > len(line):
            break
#    import re  # Can't use this
#    count = len(re.findall(word, line))
#    print(word, count)
    return count

if __name__ == '__main__':
    s = input()
    minion_game(s)
