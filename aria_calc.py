import math

def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width)/cover)
    print(f"You'll need {number_of_cans} cans of paint.")
    


test_h = int(input("Height of the wall: "))
test_w = int(input("Weight of the wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
