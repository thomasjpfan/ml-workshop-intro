from sklearn.svm import SVR

svr_unscaled = SVR()

svr_unscaled.fit(X_train, y_train)

svr_unscaled.score(X_test, y_test)

svr_scaled = SVR()
svr_scaled.fit(X_train_scaled, y_train)

svr_scaled.score(X_test_scaled, y_test)
