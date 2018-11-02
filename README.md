# Decision-Tree-CART
Decision tree implementation from scratch

- project folder structure :
  - DecisionTree - contains the implemntation of decision tree
  - Test  - contain the classification model build based on top of iris dataset (comparision with sklearn version of decision tree)
          - no parameter tunning is performed
  
- Python version : v3.6
- dependency : numpy v1.13.1

#### output
- Our Model Accuracy : 0.7368421052631579
- SK-Learn Model Accuracy : 0.7631578947368421

#### Future #todo task:
  - Analyse the reson for the performance deviation with sklearn(76 % accuracy) to 73 % accuracy.
  - use other performance metric - right now its a raw accuracy number used for comaprision
  - test on more dataset fro UCI machine learning repository
  - implement tree purning technique to reduce overfitting
  - adapt tree for regression by creating differnt mechanism for creating terminal node
  - try cross entropy for evaluting the split
  - 
