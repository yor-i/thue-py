import sys, random

lines = open(sys.argv[1]).readlines()

# Dictionary storing all substrings and their replacements like so:
# {<substring>: [<replacement1>, <replacement2>, ...]}
dty = {}

# Initial input on last line
inp = lines[-1]

for l in lines:
    if "::=" in l:
        org = l.split("::=")[0].replace('\n', '')
        rep = l.split("::=")[1].replace('\n', '')

        if org not in dty.keys():
            dty[org] = [rep]
        else:
            dty[org].append(rep)

while True:
    # A list of all substrings which can be replaced
    matching = []

    for e in list(dty.keys())[:-1]:
        if e in inp:
            matching.append(e)

    # If nothing can be replaced exit
    if matching == []:
        break

    # Choose a substring to replace and what to replace it with
    org = random.choice(matching)
    rep = random.choice(dty[org])
    
    # Handle IO and string replacement
    if rep[0] == '~':
        print(rep[1:])
        inp = inp.replace(org, '')
    elif rep == ":::":
        inp = inp.replace(org, input("> "))
    else:
        inp = inp.replace(org, rep)