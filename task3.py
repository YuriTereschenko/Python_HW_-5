"""Отфильтруйте его, чтобы этот текст можно было нормально прочесть. Предусмотрите вариант, что мусорные слова могли
 быть написаны без использования запятых."""


def text_filter(txt, what_exclude):
    txt = txt.split()
    for i in what_exclude:
        for j in txt:
            if i in j.lower():
                txt.remove(j)

    result = str(f"{txt[0]} ")
    for i in txt[1:]:
        result += f"{i} "
    return result


input_text = "Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, " \
             "было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, " \
             "эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, " \
             "жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, " \
             "в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в " \
             "магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел " \
             "другой дорогой и не упал в эту… ээээ… яму. Хлеба купил"

words_parasites = ["ну", "короче", "эээ", "эээээ", "кажется"]
print(text_filter(input_text, words_parasites))
