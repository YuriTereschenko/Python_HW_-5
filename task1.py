"""Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо.
Выполните ее в виде функции.
Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»"""

def text_filter(text, what_exclude):
    temp = text.split()
    temp = list(filter(lambda x: what_exclude.lower() not in x.lower(), temp))
    if len(temp) > 0:
        result = f"{temp[0]} "
        for i in temp[1:]:
            result += f"{i} "
    print(result)


text_filter("абвгдеж рабав копыто фабв Абкн абрыволк аБволк", "абв")

