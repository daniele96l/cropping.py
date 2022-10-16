import pandas as pd
import csv
from operator import itemgetter

with open("kaggle2.txt", "r") as myfile:
    data = myfile.read().splitlines()

new_data = []
s = ""
i = 0
for row in data:
    new_data.append(str(s))
    new_data[i] += str(row)
    i += 1

new_listA = [s.replace(" ", "") for s in new_data]
new_listB = [s.replace("[", "") for s in new_listA]
new_list2 = [s.replace("]", ",") for s in new_listB]
new_list3 = [s.replace("'", "") for s in new_list2]

new_list4 = []
for i in new_list3:
    if (len(i) < 20):
        i += ","
        i += ","
        i += ","
        i += ","
        i += ","
        new_list4.append(i.split(","))
    else:
        new_list4.append(i.split(","))

new_list5 = new_list4
y = 0

# take the frame number
for i in new_list4:
    frame = i[5].split("/")[4]
    num = frame.split("_")[2]
    # print(num)
    new_list5[y][5] = int(num)
    y += 1
    # print(y)

# order according to the frame number
sorted_list = sorted(new_list5, key=itemgetter(5))
sorted_list2 = pd.DataFrame(sorted_list)
sorted_list2[4] = sorted_list2[4].str[5:-4]

new_col = pd.read_csv('dati_mappa.csv')

print(new_col)

beginning = "PosixPath('/exp/datasets/Cam1/202107280658_Rectified_"
end = "_Cam1.jpg')]"
#rilevamenti_original.txt
#[0.429931640625, 0.49346405267715454, 0.00634765625, 0.0049019609577953815, 'regulatory--yield--g1 0.44', PosixPath('/exp/datasets/Cam1/202107280658_Rectified_1000_Cam1.jpg')]

for i in range(len(sorted_list2)):
    x = sorted_list2.iloc[i][5]
    x = beginning + str(x) + end
    sorted_list2.iloc[i,5] = x
    sorted_list2.iloc[i,0] = "[" + sorted_list2.iloc[i][0] + ","
    sorted_list2.iloc[i,1] =  sorted_list2.iloc[i][1] + ","
    sorted_list2.iloc[i,2] =  sorted_list2.iloc[i][2] + ","
    sorted_list2.iloc[i,3] =  sorted_list2.iloc[i][3] + ","
  
    

sorted_list2.drop(columns = [6], axis = 1, inplace = True)
sorted_list2.drop(columns = [4], axis = 1, inplace = True)

sorted_list2["Class"] = "'" +new_col + str(" 0.55") +"',"


sorted_list2[5], sorted_list2["Class"] = sorted_list2["Class"],sorted_list2[5]



x = pd.DataFrame.to_string(sorted_list2,columns=[0,1,2,3,5,"Class"], header=False,index=False,col_space = 0)

with open('kaggle2.txt', 'w') as f:
        f.write(x)



print("Hello")