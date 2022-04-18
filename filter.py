# with open('words.txt') as word_file:
#     words = word_file.read().split()
#     print(len(words))
#     valid_words = []
#     for word in words:
#         if len(word) == 5 and word.isalpha() == True:
#             # repeat = False
#             # for i in range(5):
#             #     if i != word.rfind(word[i]):
#             #         repeat = True
#             # if not repeat:
#             #     valid_words.append(word.upper())
#             valid_words.append(word.upper())
#     print(len(valid_words))
#     with open('valid_words.txt', 'w') as valid_words_file:
#         for valid_word in valid_words:
#             valid_words_file.write(valid_word + '\n')
import json

with open('word5.json') as word_file:
    words = json.load(word_file)
    print(len(words))
    with open('valid_words.txt', 'w') as valid_words_file:
        for word in words:
            valid_words_file.write(word['word'].upper() + '\n')
