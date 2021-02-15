# Andrew Enrique Oliveira
# Ciência da Computação - Universidade Federal de Itajubá (2017 - )
# 15/02/2021
#
# Os conteúdos de todas as funções, exceto a main, foram implementados por mim

import csv
import sys
from sklearn import neighbors

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils.validation import _num_samples

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")

def month_to_int(string):
    m = {
            'jan': 0,
            'feb': 1,
            'mar': 2,
            'apr': 3,
            'may': 4,
            'jun': 5,
            'jul': 6,
            'aug': 7,
            'sep': 8,
            'oct': 9,
            'nov': 10,
            'dec': 11
        }
    s = string.strip()[:3].lower()

    return m[s]

def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = list()
    labels = list()

    with open(filename, newline='') as data_file:
        file_reader = csv.reader(data_file, delimiter=',')
        for i, row in enumerate(file_reader):
            element_list = list()

            if i == 0:
                continue
            else:
                for j, column_value in enumerate(row):
                    if (j%2 != 0 and j < 6) or (j > 5 and j < 10):
                        element_list.append(float(column_value))
                    elif j == 10:
                        element_list.append(month_to_int(column_value))
                    elif j == 15:
                        element_list.append(1) if column_value == 'Returning_Visitor' else element_list.append(0)
                    elif j == 16:
                        element_list.append(1) if column_value == 'TRUE' else element_list.append(0)
                    elif j == 17:
                        labels.append(1) if column_value == 'TRUE' else labels.append(0)
                    else:
                        element_list.append(int(column_value))
                    
                evidence.append(element_list)
    
    return evidence, labels


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    total_trues = labels.count(1)
    total_falses = labels.count(0)
    correct_trues = 0
    correct_falses = 0

    for i, value_l in enumerate(labels):
        if predictions[i] == value_l:
            if value_l == 1:
                correct_trues += 1
            else:
                correct_falses += 1
    
    # return sensitivity, specificity
    return correct_trues/total_trues, correct_falses/total_falses

if __name__ == "__main__":
    main()
