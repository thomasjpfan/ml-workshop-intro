from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

wine = load_wine(as_frame=True)
X, y = wine.data, wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, stratify=y)

knc = KNeighborsClassifier()
knc.fit(X_train, y_train)
knc.score(X_test, y_test)

rfc = RandomForestClassifier(random_state=0)
rfc.fit(X_train, y_train)
rfc.score(X_test, y_test)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
log_reg.score(X_train, y_train)