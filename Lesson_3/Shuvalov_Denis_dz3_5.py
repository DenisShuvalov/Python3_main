from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "слон"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "скоро"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "осений"]
list_min = min(nouns, adverbs, adjectives)


def print_jokes(n, repeat=False):
    nouns_second = nouns.copy()
    adverbs_second = adverbs.copy()
    adjectives_second = adjectives.copy()
    list_of_jokes = []
    list_min = min(nouns_second, adverbs_second, adjectives_second)

    while n and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            list_of_jokes.append(f"{nouns_second.pop(num)} {adverbs_second.pop(num)} {adjectives_second.pop(num)}")
        else:
            list_of_jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n = n - 1
    return list_of_jokes


n = int(input('Введите количество шуток: '))
i = 1
print_jokes(n, i)

if n <= len(list_min):
    print(print_jokes(n, True))
else:
    print("Слишком много")
