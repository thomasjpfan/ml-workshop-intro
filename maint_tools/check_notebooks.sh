set -xe

jupyter nbconvert --execute notebooks/0*.ipynb --to notebook --stdout
