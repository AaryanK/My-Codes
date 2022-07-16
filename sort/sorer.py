import pandas as pd

df = pd.read_csv('BE-BArch-Admission-2077-Applicant-Priroty-List-After-Change.csv')
df.set_index('Rank',inplace=True)
df.sort_index(inplace=True)


# For regular computer students
raw_comp = df[df['p2']==2]
raw_civil_pay = df[df['p1']==2] 
regular_list = list(raw_comp['Roll NoApplicant Name'].head(86))
pay_list = list(raw_civil_pay['Roll NoApplicant Name'].head(84)) 
final_list = []
final_list.extend(regular_list)
final_list.extend(pay_list)



def check_priority(priority):
    raw_comp = df[df['p2']==2]
    raw_civil_pay = df[df['p1']==2] 
    regular_list = list(raw_comp['Roll NoApplicant Name'].head(86))
    pay_list = list(raw_civil_pay['Roll NoApplicant Name'].head(84)) 
    final_list = []
    final_list.extend(regular_list)
    final_list.extend(pay_list)

number = 1
# comp_list = sorted(comp_list)
for i in final_list:
    '''print(f"Number {number} {i}")
    number = number+1'''

    if i == "555 ASHWIN DAWADI":
        print(f"Rank is {final_list.index(i)+1}")