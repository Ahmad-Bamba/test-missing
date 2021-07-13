import pandas as pd
import random

genders = ['male', 'female', 'non-binary']
ethnicities = ['white', 'white-latino', 'native', 'asian', 'black']

df = pd.read_csv('data/FL_insurance_sample.csv')

def return_ethnicity(row):
    x = random.randint(1, 100)
    if x < 75: 
        return random.choice([ethnicities[0], ethnicities[1]])
    if x < 90:
        return ethnicities[4]
    return random.choice([ethnicities[2], ethnicities[3]])

def return_gender(row):
    x = random.randint(1, 100)
    if x < 45:
        return genders[0]
    if x < 90:
        return genders[1]
    return genders[2]
    

df['gender'] = df.apply(return_gender, axis=1)
df['race'] = df.apply(return_ethnicity, axis=1)

print(df.head(10))

df.to_csv('data/test_data.csv')
