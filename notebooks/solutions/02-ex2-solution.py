from sklearn.datasets import load_wine

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

X, y = load_wine(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y)

kn = KNeighborsClassifier()
rf = RandomForestClassifier()
lr = LogisticRegression()

kn.fit(X_train, y_train)
rf.fit(X_train, y_train)
lr.fit(X_train, y_train)

print("kn train: ", kn.score(X_train, y_train))
print("rf train: ", rf.score(X_train, y_train))
print("lr train: ", lr.score(X_train, y_train))

print("kn test: ", kn.score(X_test, y_test))
print("rf test: ", rf.score(X_test, y_test))
print("lr test: ", lr.score(X_test, y_test))
