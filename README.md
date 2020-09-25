# Introduction to scikit-learn: Machine Learning in Python

[Link to slides](https://thomasjpfan.github.io/ml-workshop-intro/)

## About the workshop

Scikit-learn is a machine learning library in Python that is used by many data science practitioners. Machine learning is a valuable tool used across many domains such as medicine, physics, and finance. We will start this training by learning about scikit-learn’s API for supervised machine learning. scikit-learn's API mainly consists of three methods: fit, to build models, predict, to make predictions from models, and transform, to change the representation of the input data. Supervised machine learning models in scikit-learn that make predictions are called classifiers or regressors. Models that are used for transforming data are called transformers. This simple and consistent interface helps to abstract away the algorithm, thus allowing us to focus on our particular problems. We will use this interface to apply traditional machine learning algorithms such as linear models and tree based models. We will learn about the importance of splitting your data into train and test sets for model evaluation. Next, we will learn about preprocessing numerical data and its importance for certain machine learning models. For example, preprocessing is important for models that compute distances such as nearest neighbor models. Finally, we will learn how to combine these preprocessing techniques with a machine learning model by using a Pipeline. The Pipeline enables us to combine transformers with a classifier or regressor to build a data flow, where the output of one layer is the input or another. After this workshop, you will be able use and apply scikit-learn to your machine learning problems.

## License

This repo is under the [MIT License](LICENSE).
