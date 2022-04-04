# pygsheets-examples

An examples of using service account credentials for accessing Google Sheets with pygsheets

See the following _for background_

- https://pygsheets.readthedocs.io/en/stable/
- https://pygsheets.readthedocs.io/en/stable/authorization.html
- https://github.com/ontodev/cogs#credentials

Requires python 3.9

## Steps to install and run

- `git clone` this repo
- Ask your contact person to email `biosamples-annotation-dg-32fd479a2039.json` to you
- Place `biosamples-annotation-dg-32fd479a2039.json` in this project's `local` directory
- [Install the poetry application if necessary](https://python-poetry.org/docs/#installation)
- Use poetry to install the project dependencies: `poetry install`
- Run some code to print out a sample Google Sheet: `make print_sheet`


## Want to reuse some of this for a different sheet?

You will need to tell Google Sheets that people with `biosamples-annotation-dg-32fd479a2039.json` are allowed to access your sheet. 

You do that by clicking on the green `share` button in the upper right corner of the Google Sheets screen and entering the following email address: `biosamples-annotation-dg-sa@biosamples-annotation-dg.iam.gserviceaccount.com`. (That's the value of the `client_email` key in `biosamples-annotation-dg-32fd479a2039.json`)

