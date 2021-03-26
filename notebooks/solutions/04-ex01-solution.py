
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer(as_frame=True)

X, y = cancer.data, cancer.target

y.value_counts()

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                                                   random_state=0)

from sklearn.linear_model import LogisticRegression

log_reg = make_pipeline(
    StandardScaler(),
    LogisticRegression(random_state=0)
)

log_reg.fit(X_train, y_train)

log_reg.score(X_test, y_test)

log_reg_poly = make_pipeline(
    StandardScaler(),
    PolynomialFeatures(),
    LogisticRegression(random_state=0)
)

log_reg_poly.fit(X_train, y_train)

log_reg_poly.score(X_test, y_test)
