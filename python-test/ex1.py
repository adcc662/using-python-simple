def count_occurrences(paragraph: str, word: str):
    word_length = len(word)
    count = 0
    index = 0

    while index < len(paragraph):
        match = True
        for i in range(word_length):
            if index + i >= len(paragraph) or paragraph[index + i].lower() != word[i].lower():
                match = False
                break
        if match:
            count += 1
            index += word_length
        else:
            index += 1

    return count

paragraph = """
La logística Digital es un concepto que surge de la integración entre la logística tradicional y
la era digital. Con el auge del correo electrónico y las descargas digitales reemplazando
productos físicos, podríamos estar hablando de un golpe devastador para la industria de la
logística, pero, de hecho, ha ocurrido algo muy diferente. El sector de la logística ha
introducido las innovaciones digitales.
"""

word_to_find: str = "logística"
result: int = count_occurrences(paragraph, word_to_find)
print(f'{result} ocurrencias encontradas')