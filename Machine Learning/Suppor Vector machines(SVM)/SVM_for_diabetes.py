import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.tree import export_graphviz
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


if __name__ == '__main__':
    col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
    # load data
    pima = pd.read_csv(r'C:\Users\83549\Github Projects\Algorithm\Machine Learning\Suppor Vector machines(SVM)\Data\diabetes.csv', header=0, names=col_names)
    print(pima.head())


    # feature selection
    feature_cols = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
    X = pima[feature_cols]
    y = pima.label
    print(X)
    print(y)

    # Splitting Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% for training and 30% for testing

    # Buliding SVM Model
    # we create an instance of SVM and fit out data. We do not scale our data since we want to plot the support vectors
    C = 1.0  # SVM regularization parameter
    svc = svm.SVC(kernel='linear', C=C).fit(X_train, y_train)
    #rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X_train, y_train)
    poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X_train, y_train)
    #lin_svc = svm.LinearSVC(C=C).fit(X_train, y_train)

    # The linear models LinearSVC() and SVC(kernel='linear') yield slightly different decision boundaries. This can be a consequence of the following differences:

    # LinearSVC minimizes the squared hinge loss while SVC minimizes the regular hinge loss.
    # LinearSVC uses the One-vs-All (also known as One-vs-Rest) multiclass reduction while SVC uses the One-vs-One multiclass reduction.


    y_pred = svc.predict(X_test)
    #y_pred_rbf = rbf_svc.predict(X_test)
    y_pred_poly = poly_svc.predict(X_test)
    #y_pred_lin = lin_svc.predict(X_test)

    # Evaluating Model
    print("Normal SVC Accuracy:", metrics.accuracy_score(y_test, y_pred))
    #print("RBF SVC Accuracy:", metrics.accuracy_score(y_test, y_pred_rbf))
    print("Ploy SVC Accuracy:", metrics.accuracy_score(y_test, y_pred_poly))
    #print("Linear SVC Accuracy:", metrics.accuracy_score(y_test, y_pred_lin))

    
    mat = confusion_matrix(y_test, y_pred)
    sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=['Is not Diabetes', 'Diabetes'],
            yticklabels=['Is not Diabetes', 'Diabetes'])
    plt.xlabel('true label')
    plt.ylabel('predicted label');
    plt.show()
    
    