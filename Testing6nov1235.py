import pandas as pd
col = [0,1,2,3,4,5,6,7]
cse_103 = pd.read_excel("H:\\Year-1-Sem-1-2016.xlsx", skiprows=125, usecols=col, nrows=62)

i = 1
temp103 = []

a = int(abs(cse_103.iloc[i:i + 1]['Internal'] - cse_103.iloc[i:i + 1]['3rd Examiner']))
b = int(abs(cse_103.iloc[i:i + 1]['External'] - cse_103.iloc[i:i + 1]['3rd Examiner']))
if a < b:
    temp103.append(int((cse_103.iloc[i:i + 1]['Internal'] + cse_103.iloc[i:i + 1]['3rd Examiner']) / 2))
else:
    temp103.append(int((cse_103.iloc[i:i + 1]['External'] + cse_103.iloc[i:i + 1]['3rd Examiner']) / 2))

print(a)
print(b)
x = 8
#print(temp103+x)










#print(cse_101)
print(cse_103.loc[:, 'External'])
#print(cse_101.iloc[:, 1:2])
#print(cse_101[['Internal','External']])
#k=8
#print(cse_101.iloc[k:k+1]['Internal'])
#print(cse_101.iloc[k:k + 1]['External'])
#print(abs(cse_101.iloc[k:k + 1]['Internal'] - cse_101.iloc[k:k + 1]['3rd Examiner']))
#sum['Total'] = cse_101['Internal'] + cse_101['External']
#print(cse_101['Internal'])
#
#temp1 = []
#k=4
#a = (cse_101.iloc[k:k + 1]['Internal'] + cse_101.iloc[k:k + 1]['External'])/2
#print(a)

##[df = pd.DataFrame(, columns = ['First_name', 'Last_name', 'Marks'])
##k=0
##temp1.iloc[k:k+1]['Avg'] = (cse_101.iloc[k:k + 1]['Internal'] + cse_101.iloc[k:k + 1]['External'])/2
##print(temp1['Avg'])]


##temp1= []
##for i in range(62):
    #j = cse_101[i:i+1]['Difference']
   # k=i
   # a = abs(cse_101.iloc[k:k + 1]['Internal'] - cse_101.iloc[k:k + 1]['3rd Examinar']);
    #b = abs(cse_101.iloc[k:k + 1]['External'] - cse_101.iloc[k:k + 1]['3rd Examinar']);
    #if a < b:
      #  temp1['Avg'] = (cse_101.iloc[k:k + 1]['Internal'] + cse_101.iloc[k:k + 1]['3rd Examinar']) / 2;
    #else:
     #   temp1['Avg'] = (cse_101.iloc[k:k + 1]['External'] + cse_101.iloc[k:k + 1]['3rd Examinar']) / 2;

##temp =[]




#print(cse_101.head( 4)) - FOr printing upto  4 columns
#print(cse_101.loc[0:2 , :] - for printing specific row
#print(cse_101.loc[ : , 'Internal'])  - for printing specific column
#print(cse_101.loc[ : , 'Internal': 'Average'])