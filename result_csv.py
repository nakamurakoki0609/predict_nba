import pandas as pd




def add_result(result,correct):
    result_csv = pd.read_csv('result.csv')
    result_csv.loc[len(result_csv)] = [result,correct]
    result_csv.to_csv('result.csv',index=False)
    
def percent_correct():
    result_csv = pd.read_csv('result.csv')
    total  = len(result_csv)
    right_number = result_csv['correct'] == True
    per_correct = right_number.sum() / total

    return str(round(per_correct,4)*100)