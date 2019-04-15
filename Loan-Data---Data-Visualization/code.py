# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading data
data = pd.read_csv(path)

# having a brief look at data
print(data.head())

# getting info about columns in data
print(data.info())

# getting counts of Loan_Status
loan_status = data.Loan_Status.value_counts()

# plotting value counts of Loan_Status in a bar graph
loan_status.plot(kind='bar')
plt.title('Counts of people with different loan status')
plt.xlabel('Loan status')
plt.ylabel('No of people')
plt.show()


#Code starts here


# --------------
#Code starts here

# grouping loan data by property_area and loan_status
property_and_loan = data.groupby(['Property_Area','Loan_Status'])
property_and_loan = property_and_loan.size().unstack()

# plotting graph
property_and_loan.plot(kind = 'bar', stacked = False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.title('Loan distribution accross regions')
plt.xticks(rotation = 45)


# --------------
#Code starts here

# grouping data on Education and Loan_Status 
education_and_loan = data.groupby( ['Education','Loan_Status'] )
education_and_loan = education_and_loan.size().unstack()

# plotting graph
education_and_loan.plot( kind = 'bar', stacked = True )
plt.xlabel( 'Education Status' )
plt.ylabel( 'Loan Status' )
plt.title( 'Effect of education on loan approvals' )
plt.xticks( rotation = 45 )


# --------------
#Code starts here

# selecting people who are graduates
graduate = data[data['Education'] == 'Graduate']

# selecting people who are not graduates
not_graduate =  data[data['Education'] == 'Not Graduate']

# plotting graduates data
graduate.LoanAmount.plot(kind = 'density', label='Graduate')
not_graduate.LoanAmount.plot(kind = 'density', label='Not Graduate')
plt.title('Effect of education on loan amount')

#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1)

# plotting scatter plot for ApplicantIncome and LoanAmount 
ax_1.scatter( x = data['ApplicantIncome'], y = data['LoanAmount'] )
ax_1.set_title('Effect of income on loan amount')
ax_1.set_xlabel('Applicant Income')
ax_1.set_ylabel('Loan Amount')

# plotting scatter plot between CoapplicantIncome and LoanAmount 
ax_2.scatter( x = data['CoapplicantIncome'], y = data['LoanAmount'] )
ax_2.set_title('Effect of coapplicant income on loan amount')
ax_2.set_xlabel('Coapplicant Income')
ax_2.set_ylabel('Loan Amount')

# calculating total income
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

# plotting scatter plot for total of applicant and coapplicant income vs loan amount
ax_3.scatter( x = data['TotalIncome'], y = data['LoanAmount'] )
ax_3.set_title('Effect of total income on loan amount')
ax_3.set_xlabel('Total Income')
ax_3.set_ylabel('Applicant Income')


