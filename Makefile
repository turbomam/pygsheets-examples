.PHONY: print_sheet

print_sheet:
	poetry run python pygsheets-examples-1.py \
		--json_auth_file local/biosamples-annotation-dg-32fd479a2039.json
