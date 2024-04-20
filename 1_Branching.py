#Ooremide Adegbola
#Comp163 section 2
#2/7/24
#Will be writting to calculate U.S. income tax owed given wages, 
#taxable interest, unemployment compensation, status (single or married) and taxes withheld. 

#User Input
wages = int(input("Wages: "))
taxable_interest = int(input("Taxable interest: "))
unemployment_compensation = int(input("Unemployment compensation: "))
marital_status = int(input("Marital status (1 single / 2 married): "))
taxes_withheld = int(input("Taxes Withheld: "))

#Calculate AGI
agi = wages + taxable_interest + unemployment_compensation
print(f'AGI: ${agi:,}')


#Error if agi is is greater than 120000
if agi > 120000:
    print("Error: Income too high to use this form")
else:
    #Identify deduction amount based on marital status
    deduction = 12000 if marital_status == 1 else 24000

    #Calculate taxable income
    deduction = 0

    #Calculate tax amount based on deduction and taxable income
    if marital_status == 1:
        deduction = 12000
    elif marital_status == 2:
        deduction = 24000
    else:
        marital_status = 1
        deduction = 12000

    print(f'Deduction: ${deduction:,}')


    taxable_income = agi - deduction

    if taxable_income < 0:
        taxable_income = 0

    print(f'Taxable income: ${taxable_income:,}')


    tax_amount = 0
    #Using Tax chart on martial status and income
    if(marital_status == 1) and (0 <= taxable_income <= 10000):
        tax_amount = (taxable_income * .10)
    elif(marital_status == 1) and (10001 <= taxable_income <= 40000):
        tax_amount = (1000 + ((taxable_income - 10000)* .12))
    elif(marital_status == 1) and (40001 <= taxable_income <= 85000):
        tax_amount = (4600 + ((taxable_income - 40000)* .22))
    elif (marital_status == 1) and (taxable_income > 85000):
        tax_amount =(14500 + ((taxable_income - 85000)* .24))
    elif (marital_status == 2) and(0 <= taxable_income <= 20000):
        tax_amount = (taxable_income * .10)
    elif (marital_status == 2) and (10001 <= taxable_income <= 80000):
        tax_amount = (2000 +((taxable_income - 20000)* .12))
    elif (marital_status == 2) and (40001 <= taxable_income > 80000):
        tax_amount = (9200) + ((taxable_income - 80000)* .22)

    print(f'Federal tax: ${(int(tax_amount)):,}')

                           
    #Calculate amount of tax refund or due
    tax_due_or_refund = tax_amount - taxes_withheld

    #Output of Tax refund / Tax due
    if tax_due_or_refund < 0:
        tax_due_or_refund = tax_due_or_refund * -1
        print(f'Tax refund: ${int(round(tax_due_or_refund)):,d}')
    else:
        print(f'Tax due: ${int(tax_due_or_refund):,d}')
