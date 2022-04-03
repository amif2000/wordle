tries = [
    ('TEARS', 'oo  o'),
    ('SMITE', 'x  ox')
]

occurence = {
    'E': 11.1607,
    'M': 3.0129,
    'A': 8.4966,
    'H': 3.0034,
    'R': 7.5809,
    'G': 2.4705,
    'I': 7.5448,
    'B': 2.0720,
    'O': 7.1635,
    'F': 1.8121,
    'T': 6.9509,
    'Y': 1.7779,
    'N': 6.6544,
    'W': 1.2899,
    'S': 5.7351,
    'K': 1.1016,
    'L': 5.4893,
    'V': 1.0074,
    'C': 4.5388,
    'X': 0.2902,
    'U': 3.6308,
    'Z': 0.2722,
    'D': 3.3844,
    'J': 0.1965,
    'P': 3.1671,
    'Q': 0.1962
}

knowledge = []
for line in tries:
    letters = line[0]
    score = line[1]
    know = []
    for i in range(5):
        know.append((letters[i], score[i]))
    knowledge.append(know)

with open('valid_words.txt') as word_file:
    words = word_file.read().split()
    print(len(words))
    with open('options.txt', 'w') as options_file:
        count = 0
        options = []
        for word in words:
            fail = False
            for know in knowledge:
                for i in range(5):
                    datum = know[i]
                    letter = datum[0]
                    score = datum[1]
                    if score == ' ':
                        if word.find(letter) >= 0:
                            fail = True
                    elif score == 'x':
                        if word[i] != letter:
                            fail = True
                    else: # 'o'
                        if word[i] == letter or word.find(letter) < 0:
                            fail = True
            if not fail:
                seen = [False, False, False, False, False]
                for line in tries:
                    for i in range(5):
                        if line[0].find(word[i]) >= 0:
                            seen[i] = True
                occ = 0.0
                print(seen)
                for i in range(5):
                    if not seen[i]:
                        occ += occurence[word[i]]
                options.append((word, occ))
                count += 1
        options.sort(key=lambda tuple: tuple[1], reverse=True)
        for option in options:
            options_file.write("%s\n" % option[0])
print(count)