from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, random_state=0
)

from sklearn.linear_model import LogisticRegression

log_reg = make_pipeline(
    StandardScaler(), LogisticRegression()
)

log_reg.fit(X_train, y_train)

ridge_pipe.score(X_test, y_test)

from sklearn.preprocessing import PolynomialFeatures

log_reg_poly = make_pipeline(
    StandardScaler(),
    PolynomialFeatures(),
    LogisticRegression()
)

log_reg_poly.fit(X_train, y_train)

log_reg_poly.score(X_test, y_test)
