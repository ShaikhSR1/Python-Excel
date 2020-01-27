import pandas as pd

col103 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_103 = pd.read_excel("H:\Py Project\Year-1-Sem-1-2016", skiprows=125, usecols=col103, nrows=62)
temp103 = []
sum103 = []
for i in range(62):
    j = int(cse_103.iloc[i:i + 1]['Difference'])
    if j > 12:
        a = int(abs(cse_103.iloc[i:i + 1]['Internal'] - cse_103.iloc[i:i + 1]['3rd Examiner']))
        b = int(abs(cse_103.iloc[i:i + 1]['External'] - cse_103.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp103.append(int((cse_103.iloc[i:i + 1]['Internal'] + cse_103.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp103.append(int((cse_103.iloc[i:i + 1]['External'] + cse_103.iloc[i:i + 1]['3rd Examiner']) / 2))

    else:
        temp103.append(int((cse_103.iloc[i:i + 1]['Internal'] + cse_103.iloc[i:i + 1]['External']) / 2))

    x = int(temp103[i]) + int(cse_103[i:i + 1]['Tutorial'])
    sum103.append(x)


#print(sum103)

temp203 = []

for k in range(62):
    if sum103[k] >= 80:
        temp203.append(4.0)
    elif sum103[k]>=75:
        temp203.append(3.75)
    elif sum103[k]>70:
        temp203.append(3.50)
    elif sum103[k]>=65:
        temp203.append(3.25)
    elif sum103[k]>60:
        temp203.append(3.0)
    elif sum103[k]>=55:
        temp203.append(2.75)
    elif sum103[k]>50:
        temp203.append(2.50)
    elif sum103[k]>=45:
        temp203.append(2.25)
    elif sum103[k]>40:
        temp203.append(2.0)
    else:
        temp203.append(1.0)

print(temp203)


v = int(input("Enter roll: "))
y = int(cse_103.iloc[2, 1:2])
print(y)