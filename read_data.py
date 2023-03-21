import pandas as pd
import csv

path = "ABHACARD DATA DEMO.csv"

# data = pd.read_csv(r'C:\Users\nites\OneDrive\Documents\GitHub\Jaipur-Hackathon\bedsRAJASTHAN.csv')
# df = pd.DataFrame(data, columns=['District','Oxygen Beds'])
# # print(df.head(4))


data = pd.read_csv(r'C:\Users\nites\OneDrive\Documents\GitHub\Jaipur-Hackathon\Meds price compo.csv')
df = pd.DataFrame(data, columns=['Medicines_Low', 'Price'])
# print(df.head(4))

with open('Meds price compo.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    row_count = 1
    for i in csv_reader:
        if row_count == 3:
            print(i[3], "Price Rs" , i[4])
        row_count += 1


# text = '''1. B.D.Memorial Blood Centre || Plot No. 4&98 Neelkanth colony, Ajmer road near BPCL PETROL PUMP PURANICHUNGI, Jaipur, Jaipur, Rajasthan || Plot No. 4&98 Neelkanth colony, Ajmer road near BPCL PETROL PUMP PURANICHUNGI, Jaipur, Jaipur, Rajasthan || Phone: 9887318888 ,Fax: -, Email: bdmemorialbloodbank@gmail.com || Available, O+Ve:71, B+Ve:28, A+Ve:36, O-Ve:1, AB+Ve:4, B-Ve:1 || Last Updated 06-03-2023 13:47 ||
#
#         2. Blood Centre Mahatma Gandhi Hospital || Blood Bank, M G Medical College and Hospital ,Mahatma Gandhi University of Medical Science and Technology, Sitapura,Jaipur, Jaipur, Jaipur, Rajasthan || Phone: 9116019981 ,Fax: -, Email: mghbloodbank@gmail.com || Available, O+Ve:1, B+Ve:1 || Last Updated : 20-03-2023 10:01 ||
#
#         2. Govt Bdm Sat Hosp Kotputli || Govt BDM hospital Kotputli N.N 48, Kotputli, Jaipur, Rajasthan || Phone: 9116534500 ,Fax: -, Email: bloodbankkotputli@gmail.com || Available, O-Ve:1, O+Ve:35, A+Ve:19, B+Ve:43, AB-Ve:1, AB+Ve:6, A-Ve:4, B-Ve:3 || Last Updated : 19-03-2023 11:51
# '''