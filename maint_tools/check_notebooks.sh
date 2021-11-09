set -e

for f in notebooks/0*.ipynb; do
 jupyter nbconvert --execute $f --to notebook --stdout >/dev/null
done
