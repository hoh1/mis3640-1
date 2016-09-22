weight = input('enter your weight:')
height = input('enter your height:')
weight = float(weight)
height = float(height)
bmi = weight / (height * height)
if bmi <= 18.5:
    print("your bmi is %.1f. You are underweighted." % bmi)
elif bmi < 18.5 and bmi <= 25:
    print("your bmi is %.1f. You are normal-weighted." % bmi)
elif 25 < bmi <= 29.9:
    print("your bmi is %.1f. You are overweighted." % bmi)
else:
    print("your bmi is %.1f. You are obese." % bmi)
