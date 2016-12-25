all_coins = {}
inconsistency = False

input = open("fake_coins_input.txt", "r")

def weigh(input_str):
    input_str = input_str.rstrip()
    input_split = input_str.split(" ")
    left = input_split[0]
    right = input_split[1]
    tilt = input_split[2]

    global inconsistency

    if tilt == "equal":
        for coin in left:
            all_coins[coin] = "real"
        for coin in right:
            all_coins[coin] = "real"

    if tilt == "right":
        discrepancy = True
        for coin in right:
            all_coins[coin] = "real"
        for coin in left:
            if coin in all_coins and all_coins[coin] == "real":
                pass
            else:
                all_coins[coin] = "?"
                discrepancy = False

        if discrepancy == True:
            inconsistency = True

    if tilt == "left":
        discrepancy = True
        for coin in left:
            all_coins[coin] = "real"
        for coin in right:
            if coin in all_coins and all_coins[coin] == "real":
                pass
            else:
                all_coins[coin] = "?"
                discrepancy = False

        if discrepancy == True:
            inconsistency = True


for line in input:
    weigh(line)

fake_coins = [coin for coin in all_coins if all_coins[coin] == "?"]

if inconsistency:
    print("data is inconsistent")

elif len(fake_coins) == 0:
    print("no fake coins detected")

elif len(fake_coins) == 1:
    print(str(fake_coins[0]) + " is lighter")