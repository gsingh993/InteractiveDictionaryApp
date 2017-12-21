import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s ? Enter Y for yes of N for no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn =="N":
            return "Word does not exist"
        else:
            return "Please re-enter your query"
    else:
        return "Word does not exist"
word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
    else:
        print(output)
