import pandas as pd
cars = pd.read_csv('cars.csv')
print('The first five rows with odd-numbered columns of cars')
print(cars.iloc[0:5,[0,2,4,6,8,10]])

print('\n\nThe row that contains the Model of Mazda RX4')
print(cars[cars['Model']=='Mazda RX4'])

print('\n\nThe number of cylinders (cyl) in the car model Camaro Z28')
print(cars['cyl'][cars['Model']=='Camaro Z28'])

print('\n\nThe number of cylinders (cyl) and gear type (gear) of the car models Mazda RX4 Wag, Ford Pantera L, and Honda Civic')
print(cars.loc[(cars['Model']=='Mazda RX4 Wag')|(cars['Model']=='Ford Pantera L')|(cars['Model']=='Honda Civic'),
               ['Model','cyl','gear']])