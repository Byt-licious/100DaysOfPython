import math
def calc_cans(height, width, cover):
    num_cans = (height * width)/cover
    round_up_cans = math.ceil(num_cans)

    print(f"You'll need {round_up_cans} cans of paint.")
test_h = int(input())
test_w = int(input())  
coverage = 5
calc_cans(height=test_h, width=test_w, cover=coverage)  