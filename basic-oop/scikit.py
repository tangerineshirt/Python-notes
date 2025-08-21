from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

X, Y = load_iris(return_X_y=True)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)

pipe = make_pipeline(
    StandardScaler(),
    DecisionTreeClassifier()
)

pipe.fit(X_train, Y_train)

pred = pipe.predict(X_test)

print(accuracy_score(Y_test, pred) * 100)