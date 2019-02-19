#!/usr/bin/python
#Benjamin Wiens
s = "de"
words = ["dog", "deal", "deer", "bug", "bear"]
def autocomplete(s, words):
    firstchar = ""
    firstchar2 = ""
    dict = {}
    #create a dict alphabetical categories
    for index,i in enumerate(words):
        firstchar = i[0]
        if firstchar not in dict:
            dict[firstchar] = {}
        if i not in dict[firstchar]:
            dict[firstchar][i] = ""
    #fetch suggestions that match the given letters
    firstchar2 = s[0]
    for key, value in dict[firstchar2].items():
        result = key.startswith(s)
        if result == True:
            print(key)
autocomplete(s, words)
