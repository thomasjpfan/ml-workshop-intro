.PHONY: clean

clean:
	jupyter nbconvert --clear-output --inplace notebooks/0*.ipynb

check:
	jupyter nbconvert --execute notebooks/0*.ipynb --to notebook --stdout
