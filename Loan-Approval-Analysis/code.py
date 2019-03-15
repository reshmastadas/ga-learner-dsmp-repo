# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 

# code starts here. 

# Reading from CSV.
bank = pd.read_csv(path)

# Looking at columns of bank dataframe.
print(bank.info())

# Getting Categorical data.
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

# Getting Numerical data.
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)







# code ends here


# --------------
# code starts here.

# Deleting column Loan_ID from dataframe.
banks = bank.drop( ['Loan_ID'], axis = 1, inplace = False )

# Printing dataframe info to check the column is dropped or not.
print(bank.info())

# Printing number of null values in each column.
print(banks.isnull().sum())

# Calculating mode.
bank_mode = banks.mode() 

# Seeing info before fillna.
print(banks.info())

# Fill nan values of banks with values in bank_mode.
for col_name in banks.columns: 
    banks[col_name].fillna(banks[col_name].mode()[0], inplace=True)

# Printing info after fillna
print(banks.info())

#code ends here.


# --------------
# Code starts here

''' 
Loan amount of an average person based on 
'Gender', 'Married', 'Self_Employed'
'''

# Creating pivot table to calculate avg_loan_amount
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values=['LoanAmount'],aggfunc='mean')

# code ends here



# --------------
# code starts here

# Self employed people with loan approved
loan_approved_se = banks[(banks['Self_Employed']=='Yes')]
loan_approved_se = loan_approved_se[loan_approved_se['Loan_Status']=='Y']

# Non self employed people with loan approved
loan_approved_nse = banks[banks['Self_Employed']=='No']
loan_approved_nse = loan_approved_nse[loan_approved_nse['Loan_Status']=='Y']

# % of self employed and non self employed people who got loan approved.
Loan_Status = 614
percentage_se = (loan_approved_se.shape[0]/Loan_Status)*100
percentage_nse = (loan_approved_nse.shape[0]/Loan_Status)*100

# display % result
print(percentage_se, percentage_nse)

# code ends here


# --------------
# code starts here

# convert months of loan_amount_term to years
print(banks.info())
loan_term = (banks['Loan_Amount_Term'].apply(lambda x: (x)/12))

# Convert Series to DataFrame
loan_term_df = pd.DataFrame(loan_term)

# no of people whose loan_term >= 25 
big_loan_term = (loan_term_df[loan_term_df['Loan_Amount_Term']>=25]).shape[0]

print(big_loan_term)
# code ends here


# --------------
# code starts here

# Grouping banks wrt loan_status
loan_groupby = banks.groupby('Loan_Status')

# Filtering required column
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

# Calculating mean
mean_values = loan_groupby.mean()

# printing result
print(mean_values)

# code ends here


