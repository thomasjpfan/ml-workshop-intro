from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

wine = load_wine(as_frame=True)

X, y = wine.data, wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=0, stratify=y
)

knn = KNeighborsClassifier()
rfc = RandomForestClassifier()
lr = LogisticRegression()

knn.fit(X_train, y_train)
rfc.fit(X_train, y_train)
lr.fit(X_train, y_train)

print("kn train: ", knn.score(X_train, y_train))
print("rf train: ", rfc.score(X_train, y_train))
print("lr train: ", lr.score(X_train, y_train))

print("kn test: ", knn.score(X_test, y_test))
print("rf test: ", rfc.score(X_test, y_test))
print("lr test: ", lr.score(X_test, y_test))
