from sklearn.datasets import load_wine

wine = load_wine(as_frame=True)

print(wine.DESCR)

X, y = wine.data, wine.target
y.value_counts()

wine_df = wine.frame

sns.jointplot(x="alcohol", y="hue", data=wine_df, height=10, hue='target')
