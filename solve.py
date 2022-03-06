tries = [
    ('TRAIN', 'o    '),
    ('COMET', 'xo  o')
]

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
                options_file.write(word + '\n')
                count += 1
print(count)