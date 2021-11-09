.PHONY: clean check

clean:
	jupyter nbconvert --clear-output --inplace notebooks/0*.ipynb

check:
	bash maint_tools/check_notebooks.sh
