from DecisionTree import DecisionTree as dt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

def accuracy(prediction, actual):
    """
    :param prediction:
    :param actual:
    :return accuaracy:

    Simple function to compute raw accuaracy score quick comparision.
    """
    correct_count = 0
    prediction_len = len(prediction)
    for idx in range(prediction_len):
        if int(prediction[idx]) == actual[idx]:
            correct_count += 1
    return correct_count/prediction_len
def main():
    """
    Main function
    :return:
    """
    # Prepared dataset
    # use the preloaded iris dataset from sklearn for running the decision tree
    iris = load_iris()
    feature = iris.data[:,:2]
    label = iris.target
    # split the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split(feature, label, random_state= 42)


    # Our decision tree
    decision_tree_model =  dt.DecisionTree(_max_depth = 2, _min_splits = 30)
    decision_tree_model.fit(X_train, y_train)
    prediction  = decision_tree_model.predict(X_test)



    """lets comapre preformance with sklearn decision tree based on simple accuarcy metric"""

    from sklearn.tree import DecisionTreeClassifier
    from sklearn import tree
    # decision tree from sk learn
    sk_dt_model = DecisionTreeClassifier(max_depth= 2, min_samples_split= 30)
    sk_dt_model.fit(X_train, y_train)
    sk_dt_prediction = sk_dt_model.predict(X_test)

    print("Our Model Accuracy : {0}".format(accuracy(prediction, y_test)))
    print("SK-Learn Model Accuracy : {0}".format(accuracy(sk_dt_prediction, y_test)))

    #print(list(zip(prediction, sk_dt_prediction, y_test)))

if  __name__ == "__main__":
    main()

"""Output :
Our Model Accuracy : 0.7368421052631579
SK-Learn Model Accuracy : 0.7631578947368421
"""