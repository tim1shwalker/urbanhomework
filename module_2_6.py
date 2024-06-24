def single_root_words(root_word,* other_words):
    same_words = []
    root_word = root_word.lower()

    for i in other_words:
        i = i.lower()

    if root_word.lower() in i.lower() or i.lower() in root_word.lower():
        same_words.append(i)

        return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
#Если не правильно, то укажите пожалуйста в коде, где именно. Спасибо!)
