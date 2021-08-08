#correct

basic_salary = int(input())
if basic_salary <= 10000:
    HRA = 20 ; DA = 80
elif basic_salary <= 20000:
    HRA = 25 ; DA = 90
else:
    HRA = 30 ; DA = 95
da =  basic_salary * DA / 100
hra = basic_salary * HRA / 100
gross_salary = basic_salary + da + hra
print('{:.2f}'.format(gross_salary))