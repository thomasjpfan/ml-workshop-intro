wine = load_wine(as_frame=True)

print(wine.DESCR)

X, y = wine.data, wine.target

X.shape

y.unique()

wine_df = wine.frame

sns.jointplot(data=wine_df, x="proline", y="flavanoids", hue="target", height=8)
