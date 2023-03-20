import pandas as pd
import csv

path = "ABHACARD DATA DEMO.csv"

data = pd.read_csv(r'C:\Users\nites\OneDrive\Documents\GitHub\Jaipur-Hackathon\bedsRAJASTHAN.csv')
df = pd.DataFrame(data, columns=['District','Oxygen Beds'])
# print(df.head(4))

with open('bedsRAJASTHAN.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    row_count = 'Ajmer'
    for i in csv_reader:
        if row_count == 'Ajmer':
            print('hi')  # prints second column of third row
            break
        # row_count += 1