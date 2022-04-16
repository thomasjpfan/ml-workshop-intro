wine = load_wine(as_frame=True)

X, y = wine.data, wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

knc = KNeighborsClassifier()
knc.fit(X_train, y_train)

rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

knc.score(X_test, y_test)

rfc.score(X_test, y_test)

log_reg.score(X_test, y_test)
