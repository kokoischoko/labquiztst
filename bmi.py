def calculate_bmi(height, weight):
    print("Height =", height)
    print("Weight =", weight)
    bmi = weight / height ** 2
    print("bmi =", bmi)
    if bmi < 18.5:
        print("User is underweight")
    elif 18.5 <= bmi <= 25.0:
        print("User is normal")
    else:
        print("User is overweight")
    return 5

result = calculate_bmi(weight=57.0, height=1.73)
print(result)