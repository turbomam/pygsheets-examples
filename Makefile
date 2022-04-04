.PHONY: print_sheet

my_auth_file=/Users/MAM/Downloads/biosamples-annotation-dg-32fd479a2039.json

print_sheet:
	poetry run python pygsheets-examples-1.py \
		--json_auth_file XXX
