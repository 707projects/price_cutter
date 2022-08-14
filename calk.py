import os
# calculator that finds and exploits incongruent cash values in gambling sites
# note to self add write to log funcionality
def ask():
    start = input(" activate site? y/n : ")

    if start == "y":
        os.system("start ")
        os.system("start  Sites redacted so i dont get sued")
        os.system("start ")
    elif start == "n":
        pass
    else:
        print("bad input")
        ask()
def steam_check():
    try:
        aval = input("how much money is the hat on steam or backpack? ")
        xe = float(aval) // 2.5 # num of keys from steam
        a = float(value) // 2.5 # num of keys on REDACTED
        res = a - xe
        print(res)
        print("keys of the item on the site " + str(a))

        print("keys of the steam item " + str(xe))
        percent = float(res) / float(a) * 100
        if percent >= 10:
            print("recomend buy its", str(percent), "% PROFIT!")
        else:
            print("nope, not a profitable buy")


    except ValueError:
        pass

# Combine this with a web crawler, and I may be rich

def backpack_check():
    try:
        l = 2.5 * float(val)
        print("cash of the item on backpack " + str(l) + "$")
        meth = float(value) // 2.5
        result = float(meth) - float(val)

        percent = float(result) / float(meth) * 100
        if percent >= 10:
            print("recomend buy its", str(percent), "% PROFIT!")
        else:
            print("nope")
    except ValueError:
        pass

# Its money time home slice.

def exit_check():
    if val == "exit" or value == "exit":
        quit()
    else:
        pass
ask()
while True:
    value = input("how much money is the hat on the site? ")
    val = input("how many keys is the hat on backpack? ")
    exit_check()
    backpack_check()
    steam_check()
    exit_check()

