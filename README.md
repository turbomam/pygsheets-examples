# pygsheets-examples

An examples of using service account credentials for accessing Google Sheets with pygsheets

See the following _for background_

- https://pygsheets.readthedocs.io/en/stable/
- https://pygsheets.readthedocs.io/en/stable/authorization.html
- https://github.com/ontodev/cogs#credentials

Requires python 3.9

## Steps to install and run

- Ask your contact person to email `biosamples-annotation-dg-32fd479a2039.json` to you
- Place `biosamples-annotation-dg-32fd479a2039.json` in this project's `local` directory
- [Install the poetry application if necessary](https://python-poetry.org/docs/#installation)
- Use poetry to install the project dependencies: `poetry install`
- Run some code to print out a sample Google Sheet: `make print_sheet`
