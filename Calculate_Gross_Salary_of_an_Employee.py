''' This prohram will read Basic Salary, HRA and DA of an employee, calculate the PF on Basic Salary and finally print the PF and Gross Salary
of the employee.
Note: PF = 12% of the Basic Salary and Gross Salary = Basic Salary + HRA + DA + PF '''

bs=int(input("Enter the Basic Salary of the employee: "))
hra=int(input("Enter the HRA of the employee: "))
da=int(input("Enter the DA of the employee: "))
pf=bs/100*12
gs=bs+hra+da+pf
print("\nPF of the employee =","%.2f"%pf,"Rs")
print("Gross Salary of the employee =","%.2f"%gs,"Rs")
