numbers_dictionary = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре",
                      "five": "пять", "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять",
                      "ten": "десять"}


def num_translate(num):
    if (num[:1].isupper()) == True:
        return str(numbers_dictionary.get(num.lower())).title()
    return numbers_dictionary.get(num)


print(num_translate(input("Enter number from 0 to 10: ")))
