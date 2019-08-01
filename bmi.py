

def calc_bmi(height, weight):
    if (height == 0 or weight == 0):
        return 0
    else:
        return round(weight / (height * height / 10000), 1)
