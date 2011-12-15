# some data from http://www.census.gov/genealogy/names/names_files.html

from random import choice
from sys import stdout

from parse import START, END

def get_choice(d):
    choices = []
    for (c, num) in d.items():
        for n in range(num):
            choices.append(c)
    return choice(choices)

def capitalize(name):
    prefixes = ['mc', 'de', 'van', 'mac']
    for p in prefixes:
        if name.startswith(p):
            return ''.join(map(str.capitalize, name.partition(p)))
    return name.capitalize()

def _generate_name(stats, min_len=3):
    name = ''
    while len(name) < min_len:
        current = START
        name = ''
        while True:
            if current not in stats:
                raise Exception("%s not in stats, name is %s" % (current, name))
            c = get_choice(stats[current])
            if c == END:
                break
            name += c
            if len(name) == 1:
                raise Exception("Too short name %s, choices were %s, current is %s" % (name, choices, current))
            current = name[-3:]
    return name.capitalize()

def get_data(name_type):
    if name_type == 'male':
        from stats import male2
        return male2.data
    elif name_type == 'female':
        from stats import female2
        return female2.data
    elif name_type == 'last':
        from stats import last
        return last.data

def generate_name(name_type, min_length=3):
    data = get_data(name_type)
    n = _generate_name(data, min_length)
    return n

if __name__ == "__main__":
    for n in range(1):
        print(generate_name('female'), generate_name('last', 4))
    
    
