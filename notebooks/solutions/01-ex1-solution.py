from sklearn.datasets import load_wine

wine = load_wine(as_frame=True)
wine_df = wine.frame

sns.jointplot(data=wine_df, x="alcohol", y="hue", height=10, hue='target');