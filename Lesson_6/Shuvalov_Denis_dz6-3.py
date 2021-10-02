from json import dump
from itertools import zip_longest
from pprint import pprint

with open("users.csv", "r", encoding="utf=8") as users:
    with open("hobby.csv", "r", encoding="utf=8") as hb:

        if len(users.readlines()) >= len(hb.readlines()):
            users.seek(0)
            hb.seek(0)
            with open('dict_u_h.json', "w", encoding="utf=8") as f:
                alllist = zip_longest((" ".join(us.split(",")) for us in users), hb, fillvalue=None)
                mydict = {str(el[0]).strip(): str(el[1]).strip() for el in alllist}

                dump(mydict, f, ensure_ascii=False, indent=4)
            pprint(mydict)
        else:
            exit(1)
