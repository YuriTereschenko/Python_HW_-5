"""Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого плюс
1. Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного
большими буквами. Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях
номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется.
Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем
столбце: https://www.charset.org/utf-8
Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. С помощью reduce сложите получившиеся
числа и верните из функции в качестве ответа.
"""
from functools import reduce


def make_pair(lang, num):
    lang = list(map(lambda x: x.upper(), lang))
    return list(zip(num, lang))


def next(pairs):
    result = []
    for i in range(0, len(pairs)):
        temp = str(pairs[i][1])
        temp_sum = 0
        for j in range(0, len(temp)):
            temp_sum += ord(temp[j])
        if temp_sum % pairs[i][0] == 0:
            result.append(temp_sum)
    return reduce(lambda a, b: a + b, result)


list_of_language = ["C#", "C++", "Java", "Python", "Pascal", "Assembler", "JavaScript", "1C", "delphi", "go", "Ruby"]
number_of_language = [x for x in range(1, len(list_of_language) + 1)]
pair_num_and_lang = make_pair(list_of_language, number_of_language)
result = next(pair_num_and_lang)
print(result)

