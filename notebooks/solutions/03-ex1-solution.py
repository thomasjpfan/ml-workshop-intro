from sklearn.linear_model import Ridge

ridge = Ridge(random_state=0).fit(X_train, y_train)
ridge.score(X_test, y_test)

ridge_scaled = Ridge(random_state=0).fit(X_train_scaled, y_train)
ridge_scaled.score(X_test_scaled, y_test)
