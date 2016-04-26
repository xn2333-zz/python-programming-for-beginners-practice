#toss demo.py#
def flipper(limit):
    from random import randint
    heads = 0
    tails = 0
    counter = 0
    while counter < limit:
       flip = randint(0, 1)
       if flip == 0:
           heads = heads + 1
       else:
           tails = tails + 1

       counter = counter + 1
       if abs(heads - tails) > 200:
           break
    return (heads, tails)

def main():
    limit = int(input("Please enter flip limit: "))
    flips = flipper(limit)
    heads = flips[0]
    tails = flips[1]
    print("Heads = ",flips[0])
    print("Tails = ",flips[1])
