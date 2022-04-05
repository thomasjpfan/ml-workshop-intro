from sklearn.linear_model import SGDRegressor

sgd = SGDRegressor(random_state=0)
sgd.fit(X_train, y_train)

sgd.score(X_test, y_test)

y_pred = sgd.predict(X_test)

# Note on why r2 is negative
import numpy as np
y_pred = sgd.predict(X_test)

ss_res = np.sum((y_test - y_pred)**2)
ss_tot = np.sum((y_test - np.mean(y_test)) ** 2)

1 - ss_res / ss_tot

sgd_scaled = SGDRegressor(random_state=0)
sgd_scaled.fit(X_train_scaled, y_train)

sgd_scaled.score(X_test_scaled, y_test)
