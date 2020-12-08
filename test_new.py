import re
from random import choice
from frequency import DICT


# DICT = dict()
#
# text = open("voina-i-mir.txt", encoding="utf-8").read().replace("\n", " ")
# text = text.strip("\n").lower()
# text = re.sub(r"<(.*?)>", "", text)
# text = re.sub(r"[^а-яА-Я\s.,?!:;-]", "", text)
# text = text.replace(",", " ,").replace(".", " .").replace(":", " :").replace(";", " ;").\
#     replace("?", " ?").replace("!", " !")
# words = text.split()
#
#
# for i in range(len(words) - 2):
#     string = words[i] + " " + words[i + 1]
#     after = words[i + 2]
#     if string in DICT:
#         if after in DICT[string]:
#             DICT[string][after] += 1
#         else:
#             DICT[string][after] = 1
#     else:
#         DICT[string] = {after: 1}
#
#
# text = open("goncharow_i_a-text_0020.fb2", encoding="utf-8").read().replace("\n", " ")
# text = text.strip("\n").lower()
# text = re.sub(r"<(.*?)>", "", text)
# text = re.sub(r"[^а-яА-Я\s.,?!:;-]", "", text)
# text = text.replace(",", " ,").replace(".", " .").replace(":", " :").replace(";", " ;").\
#     replace("?", " ?").replace("!", " !")
# words = text.split()
#
#
# for i in range(len(words) - 2):
#     string = words[i] + " " + words[i + 1]
#     after = words[i + 2]
#     if string in DICT:
#         if after in DICT[string]:
#             DICT[string][after] += 1
#         else:
#             DICT[string][after] = 1
#     else:
#         DICT[string] = {after: 1}
#
#
# f = open("frequency.py", "w+", encoding="utf-8")
# f.write("DICT = {")
#
#
# for i in DICT:
#     s = f"'{i}': {str(DICT[i])}, "
#     f.write(s)
#
# f.write("}")
# f.close()


start = "это была"
length = 300
text = ""
for i in range(length):
    words = [(i, DICT[start][i]) for i in DICT[start].keys()]
    words = sorted(words, key=lambda x: x[1], reverse=True)
    print(words, words[:len(words) // 2 + 1])
    add = choice(words[:len(words) // 5 + 1])[0]  # тут можно менять пять на что-нибудь,
                                                  # чтобы увеличить или уменьшить рандом
    if add in ".,?!:;-":
        text += add
    else:
        text += " " + add
    start = start.split()[1] + " " + add
print(text)
