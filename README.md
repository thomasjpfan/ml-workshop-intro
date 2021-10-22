# Introduction to scikit-learn: Machine Learning in Python

*By Thomas J. Fan*

[Link to slides](https://thomasjpfan.github.io/ml-workshop-intro/)

Scikit-learn is a machine learning library in Python that is used by many data science practitioners. Machine learning is a valuable tool used across many domains such as medicine, physics, and finance. We will start this training by learning about scikit-learn’s API for supervised machine learning. scikit-learn's API mainly consists of three methods: fit, to build models, predict, to make predictions from models, and transform, to change the representation of the input data. This simple and consistent interface helps to abstract away the algorithm, thus allowing us to focus on our particular problems.

## Obtaining the Material

### With git

The most convenient way to download the material is with git:

```bash
git clone https://github.com/thomasjpfan/ml-workshop-intro
```

Please note that I may add and improve the material until shortly before the session. You can update your copy by running:

```bash
git pull origin master
```

### Download zip

If you are not familiar with git, you can download this repository as a zip file at: [github.com/thomasjpfan/ml-workshop-intro/archive/master.zip](https://github.com/thomasjpfan/ml-workshop-intro/archive/master.zip). Please note that I may add and improve the material until shortly before the session. To update your copy please re-download the material a day before the session.

## Running the notebooks

### Local Installation

Local installation requires `conda` to be installed on your machine. The simplest way to install `conda` is to install `miniconda` by using an installer for your operating system provided at [docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html). After `conda` is installed, navigate to this repository on your local machine:

```bash
cd ml-workshop-intro
```

Then download and install the dependencies:

```bash
conda env create -f environment.yml
```

This will create a virtual environment named `ml-workshop-intro`. To activate this environment:

```bash
conda activate ml-workshop-intro
```

Finally, to start `jupyterlab` run:

```bash
jupyter lab
```

This should open a browser window with the `jupterlab` interface.

### Run with Google's Colaboratory

If you have any issues with installing `conda` or running `jupyter` on your local computer, then you can run the notebooks on Google's Colaboratory:

1. [Loading data into machine learning](https://colab.research.google.com/github/thomasjpfan/ml-workshop-intro/blob/master/notebooks/01-loading-data.ipynb)
1. [Supervised learning with scikit-learn](https://colab.research.google.com/github/thomasjpfan/ml-workshop-intro/blob/master/notebooks/02-supervised-learning.ipynb)
1. [Preprocessing](https://colab.research.google.com/github/thomasjpfan/ml-workshop-intro/blob/master/notebooks/03-preprocessing.ipynb)
1. [Pipelines](https://colab.research.google.com/github/thomasjpfan/ml-workshop-intro/blob/master/notebooks/04-pipelines.ipynb)


## License

This repo is under the [MIT License](LICENSE).
