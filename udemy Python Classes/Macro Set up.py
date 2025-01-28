#1.27.25

#finding user macros
# User is looking to cut weight, and this code will
# generate macros for the user

user_Answer = input('what is your goal, do you want cut or bulk? ')
if user_Answer == 'cut':
    weight = int(input('Enter weight in pounds: '))
    num_cal = int(input('Enter number of calories you intend on consuming: '))
    fats = float(input('Enter fats in pounds from 25% to 30% in decimals: '))

    protein = weight * 1
    protein_cal = protein * 4

    fats_cal = num_cal * fats # calculating fats calories
    fats_cal_g = fats_cal / 9
    fats_cal_g = fats_cal_g.__round__()

    carbs = num_cal - protein_cal - fats_cal
    carbs_g = carbs / 4
    carbs_g = carbs_g.__round__()
    print(f'your macros will be Protein {protein}G | Fats {fats_cal_g}G | Carbs {carbs_g}G ')

    if fats_cal_g < 50:
        print('Your fats goal is too low, you need to be eating at least 50G of fats a day')
    else:
        print('Congradulation on setting your macros')

else:
    print('you did not enter cut')