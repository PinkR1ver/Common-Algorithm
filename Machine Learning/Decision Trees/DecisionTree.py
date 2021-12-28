import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import export_graphviz
from io import StringIO  
from IPython.display import Image  
import pydotplus

if __name__ == '__main__':
    col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
    # load data
    pima = pd.read_csv(r'/home/pinkr1ver/Documents/Github Projects/Common-Algorithm/Decision Trees/Data/diabetes.csv', header=0, names=col_names)
    print(pima.head())


    # feature selection
    feature_cols = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
    X = pima[feature_cols]
    y = pima.label
    print(X)
    print(y)

    # Splitting Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% for training and 30% for testing

    #Building Decision Tree Model
    classifer = DecisionTreeClassifier(criterion='entropy', max_depth=3)
    classifer = classifer.fit(X_train, y_train)

    y_perdict = classifer.predict(X_test)

    # Evaluating Model

    print("Accuracy:", metrics.accuracy_score(y_test, y_perdict))

    dot_data = StringIO()
    export_graphviz(classifer, out_file=dot_data, filled=True, rounded=True, special_characters=True, feature_names=feature_cols, class_names=['0', '1'])
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png(r'/home/pinkr1ver/Documents/Github Projects/Common-Algorithm/Decision Trees/Pictures/diabetes.png')
    Image(graph.create_png())

