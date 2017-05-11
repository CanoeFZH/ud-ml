import numpy as np
import pandas as pd

in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)

def predictions_3(data):
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Parch'] == 3 and passenger['Age'] < 20:
            predictions.append(0)
        elif (passenger['SibSp'] == 5 or passenger['SibSp'] == 3) and passenger['Age'] < 20:
            predictions.append(0)
        elif passenger['Sex'] == 'female':
            if passenger['Pclass'] < 3:
                predictions.append(1)
            elif passenger['Age'] >= 40 and passenger['Age'] <= 50:
                predictions.append(0)
            else:
                predictions.append(1)
        elif passenger['Sex'] == 'male':
            if passenger['Age'] <= 10:
                predictions.append(1)
            else:
                if passenger['Pclass'] == 1 and passenger['Age'] <= 40 and passenger['Age'] >= 20:
                    predictions.append(1)
                else:
                    predictions.append(0)
        else:
             predictions.append(0)
    
    return pd.Series(predictions)

predictions = predictions_3(data)


def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """
    if len(truth) == len(pred): 
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    
    else:
        return "Number of predictions does not match number of outcomes!"
    

print accuracy_score(outcomes, predictions)
