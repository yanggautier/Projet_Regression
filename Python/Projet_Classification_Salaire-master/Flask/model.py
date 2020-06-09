#from sklearn.metrics import accuracy_score
#from sklearn.metrics import classification_report, confusion_matrix
#from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

import pandas as pd
import pickle

def main(): # executer une fois pour la première fois

    data = pd.read_csv("C:/Users/yangg/Python/Projet_Classification_Salaire-master/Flask/csv/Prepo.csv", sep=';', encoding="utf-8-sig")

    X = data.drop('Classe de salaire par an', axis=1)
    y = data['Classe de salaire par an']



    model = RandomForestClassifier(n_estimators=500)

    model.fit(X, y)

    pickle.dump(model, open('../model.pkl', 'wb'))
#pickle.dump(model, open('./Flask/model.pkl', 'wb')) en windows 32bits

if __name__ == '__main__':
   main()





    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    # model_name = "RandomForestClassifier"
    # model.fit(X_train, y_train)
    # y_pred = model.predict(X_test)
    # score = cross_val_score(model, X_train, y_train)
    # accuracy = accuracy_score(y_test, y_pred)

    # print("Model: ", model_name)
    # print('Cross mean score: ', score.mean())
    # print('Accuracy: ', accuracy * 100)

    # RandomForestClassifier avec GridSearchCV
    # param_grid = {'n_estimators': [100, 200, 300, 700],'max_features': ['auto', 'sqrt', 'log2']}
    # model = RandomForestClassifier()
    # grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy')
    # grid.fit(X_train, y_train)

    #print(grid.best_estimator_)
    #grid_predictions = grid.predict(X_test)
    #print(confusion_matrix(y_test, grid_predictions))
    #print(classification_report(y_test, grid_predictions))



# Loading model to compare the results
#model = pickle.load(open('../model.pkl','rb'))



