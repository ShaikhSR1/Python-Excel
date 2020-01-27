import pandas as pd

col101 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_101 = pd.read_excel("D:\\Year-1-Sem-1-2016.xlsx", skiprows=59, usecols=col101, nrows=62)
temp101 = []
sum101 = []
for i in range(62):
    j = float(cse_101.iloc[i:i + 1]['Difference'])
    if j > 12.00:
        a = float(abs(cse_101.iloc[i:i + 1]['Internal'] - cse_101.iloc[i:i + 1]['3rd Examiner']))
        b = float(abs(cse_101.iloc[i:i + 1]['External'] - cse_101.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp101.append(float((cse_101.iloc[i:i + 1]['Internal'] + cse_101.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp101.append(float((cse_101.iloc[i:i + 1]['External'] + cse_101.iloc[i:i + 1]['3rd Examiner']) / 2))

    else:
        temp101.append(float((cse_101.iloc[i:i + 1]['Internal'] + cse_101.iloc[i:i + 1]['External']) / 2))

    x = float(temp101[i]) + float(cse_101[i:i + 1]['Tutorial(40)'])
    sum101.append(x)

temp201 = []

for k in range(62):
    if sum101[k] >= 80.00:
        temp201.append(4.0)
    elif sum101[k]>=75.00:
        temp201.append(3.75)
    elif sum101[k]>70.00:
        temp201.append(3.50)
    elif sum101[k]>=65.00:
        temp201.append(3.25)
    elif sum101[k]>60.00:
        temp201.append(3.0)
    elif sum101[k]>=55.00:
        temp201.append(2.75)
    elif sum101[k]>50.00:
        temp201.append(2.50)
    elif sum101[k]>=45.00:
        temp201.append(2.25)
    elif sum101[k]>40.00:
        temp201.append(2.0)
    else:
        temp201.append(1.0)


########################################################################################################################

col103 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_103 = pd.read_excel("D:\\Year-1-Sem-1-2016.xlsx", skiprows=125, usecols=col103, nrows=62)
temp103 = []
sum103 = []
for i in range(62):
    j = float(cse_103.iloc[i:i + 1]['Difference'])
    if j > 12.00:
        a = float(abs(cse_103.iloc[i:i + 1]['Internal'] - cse_103.iloc[i:i + 1]['3rd Examiner']))
        b = float(abs(cse_103.iloc[i:i + 1]['External'] - cse_103.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp103.append(float((cse_103.iloc[i:i + 1]['Internal'] + cse_103.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp103.append(float((cse_103.iloc[i:i + 1]['External'] + cse_103.iloc[i:i + 1]['3rd Examiner']) / 2))

    else:
        temp103.append(float((cse_103.iloc[i:i + 1]['Internal'] + cse_103.iloc[i:i + 1]['External']) / 2))

    x = float(temp103[i]) + float(cse_103[i:i + 1]['Tutorial'])
    sum103.append(x)

temp203 = []

for k in range(62):
    if sum103[k] >= 80.00:
        temp203.append(4.0)
    elif sum103[k]>=75.00:
        temp203.append(3.75)
    elif sum103[k]>70.00:
        temp203.append(3.50)
    elif sum103[k]>=65.00:
        temp203.append(3.25)
    elif sum103[k]>60.00:
        temp203.append(3.0)
    elif sum103[k]>=55.00:
        temp203.append(2.75)
    elif sum103[k]>50.00:
        temp203.append(2.50)
    elif sum103[k]>=45.00:
        temp203.append(2.25)
    elif sum103[k]>40.00:
        temp203.append(2.0)
    else:
        temp203.append(1.0)


########################################################################################################################

col105 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_105 = pd.read_excel("D:\\Year-1-Sem-1-2016.xlsx", skiprows=192, usecols=col105, nrows=62)
temp105 = []
sum105 = []
for i in range(62):
    j = float(cse_105.iloc[i:i + 1]['Difference'])
    if j > 12.00:
        a = float(abs(cse_105.iloc[i:i + 1]['Internal'] - cse_105.iloc[i:i + 1]['3rd Examiner']))
        b = float(abs(cse_105.iloc[i:i + 1]['External'] - cse_105.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp105.append(float((cse_105.iloc[i:i + 1]['Internal'] + cse_105.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp105.append(float((cse_105.iloc[i:i + 1]['External'] + cse_105.iloc[i:i + 1]['3rd Examiner']) / 2))

    else:
        temp105.append(float((cse_105.iloc[i:i + 1]['Internal'] + cse_105.iloc[i:i + 1]['External']) / 2))

    x = float(temp105[i]) + float(cse_105[i:i + 1]['Tutorial'])
    sum105.append(x)

temp205 = []

for k in range(62):
    if sum105[k] >= 80.00:
        temp205.append(4.0)
    elif sum105[k]>=75.00:
        temp205.append(3.75)
    elif sum105[k]>70.00:
        temp205.append(3.50)
    elif sum105[k]>=65.00:
        temp205.append(3.25)
    elif sum105[k]>60.00:
        temp205.append(3.0)
    elif sum105[k]>=55.00:
        temp205.append(2.75)
    elif sum105[k]>50.00:
        temp205.append(2.50)
    elif sum105[k]>=45.00:
        temp205.append(2.25)
    elif sum105[k]>40.00:
        temp205.append(2.0)
    else:
        temp205.append(1.0)


########################################################################################################################

col107 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_107 = pd.read_excel("D:\\Year-1-Sem-1-2016.xlsx", skiprows=192, usecols=col105, nrows=62)
temp107 = []
sum107 = []
for i in range(62):
    j = float(cse_107.iloc[i:i + 1]['Difference'])
    if j > 12.00:
        a = float(abs(cse_107.iloc[i:i + 1]['Internal'] - cse_107.iloc[i:i + 1]['3rd Examiner']))
        b = float(abs(cse_107.iloc[i:i + 1]['External'] - cse_107.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp107.append(float((cse_107.iloc[i:i + 1]['Internal'] + cse_107.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp107.append(float((cse_107.iloc[i:i + 1]['External'] + cse_107.iloc[i:i + 1]['3rd Examiner']) / 2))

    else:
        temp107.append(float((cse_107.iloc[i:i + 1]['Internal'] + cse_107.iloc[i:i + 1]['External']) / 2))

    x = float(temp107[i]) + float(cse_107[i:i + 1]['Tutorial'])
    sum107.append(x)

temp207 = []

for k in range(62):
    if sum107[k] >= 80.00:
        temp207.append(4.0)
    elif sum107[k]>=75.00:
        temp207.append(3.75)
    elif sum107[k]>70.00:
        temp207.append(3.50)
    elif sum107[k]>=65.00:
        temp207.append(3.25)
    elif sum107[k]>60.00:
        temp207.append(3.0)
    elif sum107[k]>=55.00:
        temp207.append(2.75)
    elif sum107[k]>50.00:
        temp207.append(2.50)
    elif sum107[k]>=45.00:
        temp207.append(2.25)
    elif sum107[k]>40.00:
        temp207.append(2.0)
    else:
        temp207.append(1.0)


########################################################################################################################

col109 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_109 = pd.read_excel("D:\\Year-1-Sem-1-2016.xlsx", skiprows=326, usecols=col109, nrows=62)
temp109 = []
sum109 = []
for i in range(62):
    j = float(cse_109.iloc[i:i + 1]['Difference'])
    if j > 12.00:
        a = float(abs(cse_109.iloc[i:i + 1]['Internal'] - cse_109.iloc[i:i + 1]['3rd Examiner']))
        b = float(abs(cse_109.iloc[i:i + 1]['External'] - cse_109.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp109.append(float((cse_109.iloc[i:i + 1]['Internal'] + cse_109.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp109.append(float((cse_109.iloc[i:i + 1]['External'] + cse_109.iloc[i:i + 1]['3rd Examiner']) / 2))

    else:
        temp109.append(float((cse_109.iloc[i:i + 1]['Internal'] + cse_109.iloc[i:i + 1]['External']) / 2))

    x = float(temp109[i]) + float(cse_109[i:i + 1]['Tutorial'])
    sum109.append(x)

temp209 = []

for k in range(62):
    if sum109[k] >= 80.00:
        temp209.append(4.0)
    elif sum109[k]>=75.00:
        temp209.append(3.75)
    elif sum109[k]>70.00:
        temp209.append(3.50)
    elif sum109[k]>=65.00:
        temp209.append(3.25)
    elif sum109[k]>60.00:
        temp209.append(3.0)
    elif sum109[k]>=55.00:
        temp209.append(2.75)
    elif sum109[k]>50.00:
        temp209.append(2.50)
    elif sum109[k]>=45.00:
        temp209.append(2.25)
    elif sum109[k]>40.00:
        temp209.append(2.0)
    else:
        temp209.append(1.0)


########################################################################################################################

col111 = [0, 1, 2, 3, 4, 5, 6, 7]
cse_111 = pd.read_excel("D:\\Year-1-Sem-1-2016.xlsx", skiprows=192, usecols=col105, nrows=62)
temp111 = []
sum111 = []
for i in range(62):
    j = float(cse_111.iloc[i:i + 1]['Difference'])
    if j > 12.00:
        a = float(abs(cse_111.iloc[i:i + 1]['Internal'] - cse_111.iloc[i:i + 1]['3rd Examiner']))
        b = float(abs(cse_111.iloc[i:i + 1]['External'] - cse_111.iloc[i:i + 1]['3rd Examiner']))
        if a < b:
            temp111.append(float((cse_111.iloc[i:i + 1]['Internal'] + cse_111.iloc[i:i + 1]['3rd Examiner']) / 2))
        else:
            temp111.append(float((cse_111.iloc[i:i + 1]['External'] + cse_111.iloc[i:i + 1]['3rd Examiner']) / 2))

    else:
        temp111.append(float((cse_111.iloc[i:i + 1]['Internal'] + cse_111.iloc[i:i + 1]['External']) / 2))

    x = float(temp111[i]) + float(cse_111[i:i + 1]['Tutorial'])
    sum111.append(x)


temp211 = []

for k in range(62):
    if sum111[k] >= 80.00:
        temp211.append(4.0)
    elif sum111[k]>=75.00:
        temp211.append(3.75)
    elif sum111[k]>70.00:
        temp211.append(3.50)
    elif sum111[k]>=65.00:
        temp211.append(3.25)
    elif sum111[k]>60.00:
        temp211.append(3.0)
    elif sum111[k]>=55.00:
        temp211.append(2.75)
    elif sum111[k]>50.00:
        temp211.append(2.50)
    elif sum111[k]>=45.00:
        temp211.append(2.25)
    elif sum111[k]>40.00:
        temp211.append(2.0)
    else:
        temp211.append(1.0)


########################################################################################################################

col108 = [0, 1, 2, 3, 4]
cse_108 = pd.read_excel("D:\\Year-1-Sem-1-2016.xlsx", skiprows=461, usecols=col108, nrows=62)
temp108 = []
sum108 = []
for i in range(62):
    x = float(cse_108[i:i + 1]['Total'])
    sum108.append(x)


temp208 = []
for k in range(62):
    if sum108[k] >= 80.00:
        temp208.append(4.0)
    elif sum108[k]>=75.00:
        temp208.append(3.75)
    elif sum108[k]>70.00:
        temp208.append(3.50)
    elif sum108[k]>=65.00:
        temp208.append(3.25)
    elif sum108[k]>60.00:
        temp208.append(3.0)
    elif sum108[k]>=55.00:
        temp208.append(2.75)
    elif sum108[k]>50.00:
        temp208.append(2.50)
    elif sum108[k]>=45.00:
        temp208.append(2.25)
    elif sum108[k]>40.00:
        temp208.append(2.0)
    else:
        temp208.append(1.0)


########################################################################################################################


col114 = [0, 1, 2, 3, 4]
cse_114 = pd.read_excel("D:\\Year-1-Sem-1-2016.xlsx", skiprows=529, usecols=col114, nrows=62)
temp114 = []
sum114 = []
for i in range(62):
    x = float(cse_114[i:i + 1]['Total'])
    sum114.append(x)


temp214 = []
for k in range(62):
    if sum114[k] >= 40.00:
        temp214.append(4.0)
    elif sum114[k] >= 37.50:
        temp214.append(3.75)
    elif sum114[k] > 35.00:
        temp214.append(3.50)
    elif sum114[k] >= 32.50:
        temp214.append(3.25)
    elif sum114[k] > 30.00:
        temp214.append(3.0)
    elif sum114[k] >= 27.50:
        temp214.append(2.75)
    elif sum114[k] > 25.00:
        temp214.append(2.50)
    elif sum114[k] >= 22.50:
        temp214.append(2.25)
    elif sum114[k] > 20.00:
        temp214.append(2.0)
    else:
        temp214.append(1.0)


########################################################################################################################

col100 = [0, 1, 2]
cse_100 = pd.read_excel("D:\\Year-1-Sem-1-2016.xlsx", skiprows=598, usecols=col100, nrows=62)
temp100 = []
sum100 = []
for i in range(62):
    x = float(cse_100[i:i + 1]['Marks'])
    sum100.append(x)

temp200 = []
for k in range(62):
    if sum100[k] >= 40.00:
        temp200.append(4.0)
    elif sum100[k] >= 37.50:
        temp200.append(3.75)
    elif sum100[k] > 35.00:
        temp200.append(3.50)
    elif sum100[k] >= 32.50:
        temp200.append(3.25)
    elif sum100[k] > 30.00:
        temp200.append(3.0)
    elif sum100[k] >= 27.50:
        temp200.append(2.75)
    elif sum100[k] > 25.00:
        temp200.append(2.50)
    elif sum100[k] >= 22.50:
        temp200.append(2.25)
    elif sum100[k] > 20.00:
        temp200.append(2.0)
    else:
        temp200.append(1.0)


########################################################################################################################

v = int(input("Enter roll: "))
sumcgpa = 0
for z in range(62):
    m = int(cse_101.iloc[z, 1:2])
    if(m==v):
        sumcgpa = ((temp201[z] * 3) + (temp203[z] * 3) + (temp205[z] * 3) + (temp207[z] * 3) + (temp209[z] * 3) + (temp211[z] * 2) + (temp208[z] * 1) + (temp214[z] * 1) + (temp200[z] * 1)) / 20
        print("Final CGPA: ", end="")
        print(round(sumcgpa, 2))
        print("CSE101 : ", end="")
        print(round(temp201[z], 2))
        print("CSE103 : ", end="")
        print(round(temp203[z], 2))
        print("CSE105 : ", end="")
        print(round(temp205[z], 2))
        print("CSE107 : ", end="")
        print(round(temp207[z], 2))
        print("CSE109 : ", end="")
        print(round(temp209[z], 2))
        print("CSE111 : ", end="")
        print(round(temp211[z], 2))
        print("CSE108 : ", end="")
        print(round(temp208[z], 2))
        print("CSE114 : ", end="")
        print(round(temp214[z], 2))
        print("CSE100 : ", end="")
        print(round(temp200[z], 2))

        break

