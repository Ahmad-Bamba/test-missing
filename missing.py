from fractions import Fraction
import pandas as pd
import operator
import math

SENSITIVE = ['gender', 'race', 'disability']

# check if any nan exists
def any_nan(dataframe):
    return dataframe.isnull().values.any()

def do_check(df_name, dataframe):
    print('Doing check for {0}...'.format(df_name))
    if any_nan(dataframe) is False:
        print('No missing values!')
        return
    print('It appears this dataframe has missing data.')
    print('Running analysis...')
    nan_cols = dataframe.columns[dataframe.isna().any()].tolist()
    print('The columns with missing values are: {}'.format(nan_cols))
    
    for sensitive in SENSITIVE:
        if sensitive in dataframe:
            print('Column {} is a sensitive column.'.format(sensitive))
            # O(n) frequency algorithm for every sensitive value
            for nan_col in nan_cols:
                sensitive_frequency = {}
                for i in range(len(dataframe[nan_col])):
                    if math.isnan(dataframe[nan_col][i]):
                        if dataframe[sensitive][i] in sensitive_frequency:
                            sensitive_frequency[dataframe[sensitive][i]] += 1
                        else:
                            sensitive_frequency[dataframe[sensitive][i]] = 1
                largest_frequency = max(sensitive_frequency.items(), key=operator.itemgetter(1))[0]
                val_largest_frequency = sensitive_frequency[largest_frequency]
                val_all_missing = dataframe[nan_col].isna().sum()
                print('For column {0}, missing entries most had the {1} value of {2},' 
                    ' which is {3} (~{4}) of all missing data'.format(nan_col, sensitive, largest_frequency, 
                                                                Fraction(val_largest_frequency, val_all_missing),
                                                                '{:.0%}'.format(val_largest_frequency / val_all_missing)))
        else:
            print('Potential sensitive value {} not found'.format(sensitive))            
    print('Done!\n')


if __name__ == '__main__':
    df_blind = pd.read_csv('data/blind_missing.csv')
    df_biased = pd.read_csv('data/biased_missing.csv')

    do_check('Blind Missing', df_blind)
    do_check('Biased Missing', df_biased)
