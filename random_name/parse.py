START = 0
END = 1

def add_or_increment(dictionary, prev, current):
    """The dictionary should keep track of how many times the current value occurs after the previous value"""
    if prev == START and len(current) < 3:
        raise Exception("%s is too short" % current)
    if prev not in dictionary:
        dictionary[prev] = {current: 1} # first time we see the previous value, add it
    elif current not in dictionary[prev]:
        dictionary[prev][current] = 1 # first time we see this value, set it to one
    else:
        dictionary[prev][current] += 1 # otherwise, just increment

def gen_stats(list):
    stats = {}
    for word in list:
        if len(word) < 3:
            pass
        elif len(word) == 3:
            add_or_increment(stats, START, word)
            add_or_increment(stats, word, END)
        else:
            chars = word[:3]
            add_or_increment(stats, START, chars)
            for i in range(3,len(word)):
                chars += word[i]
                add_or_increment(stats, chars[:3], chars[3])
                chars = chars[1:]
                if len(chars) == 1:
                    raise Exception("%s is too short" % word)
            add_or_increment(stats, chars[:3], END)
    return stats

if __name__ == "__main__":
    # csv
    # f = open('data.csv') # first line = males, second = females
    # data = f.readline() # male
    # data_female = f.readline()
    # f.close()
    # names = [s.lower() for s in data.split(",")]

    # line based
    f = open('last.txt')
    names = [s.lower() for s in f.read().splitlines()]
    f.close()

    stats = gen_stats(names)

    print("data = %s" % stats)
