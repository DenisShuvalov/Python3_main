names_list = "Иван", "Мария", "Петр", "Илья", "Влада", "Виталий", "Наталья", "Нина"
names_first_character = []
names_capital_character = {}


def thesaurus(names_list):
    def same_capital_letters_sch(names_list):
        return names_list.startswith(names)

    for i in sorted(names_list):
        names_first_character.append(names_list[names_list.index(i)][:1])
        names = names_list[names_list.index(i)][:1]
        name_staff_test = list(filter(same_capital_letters_sch, names_list))
        names_capital_character[names] = name_staff_test
    return names_capital_character


print(thesaurus(names_list))
