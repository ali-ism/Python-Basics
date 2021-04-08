def make_change(due, paid):
    change = paid - due
    hundred = 0
    fifty = 0
    twenty = 0
    ten = 0
    five = 0
    one = 0
    half = 0
    quarter = 0
    while change >= 100:
        change -= 100
        hundred += 1
    while change >= 50:
        change -= 50
        fifty +=1
    while change >= 20:
        change -= 20
        twenty +=1
    while change >= 10:
        change -= 10
        ten +=1
    while change >= 5:
        change -= 5
        five +=1
    while change >= 1:
        change -= 1
        one +=1
    while change >= 0.5:
        change -= 0.5
        half +=1
    while change >= 0.25:
        change -= 0.25
        quarter +=1
    print(f"{hundred} hundreds, {fifty} fifties, {twenty} twenties, {ten} tens, {five} fives, {one} ones, {half} halves and {quarter} quarters")
#

due = 200
paid = 675
make_change(due, paid)