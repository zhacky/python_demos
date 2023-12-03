def toCamelCase(word):
    words = word.split("_")
    result = ""
    for (i, w) in enumerate(words):
        if i == 0:
            result = w
        else:
            result += w.capitalize()

    return result
