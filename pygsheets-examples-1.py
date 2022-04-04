import click
import pygsheets


# also requires pandas
# service_account_credentials_json = '/Users/MAM/Downloads/biosamples-annotation-dg-32fd479a2039.json'
# # see https://pygsheets.readthedocs.io/en/stable/authorization.html
# # and https://github.com/ontodev/cogs#credentials

# bad practices: prints sheet contents instead of using a logger or saving to a file
# the sheet name should probably also be a click argument


@click.command()
@click.option('--json_auth_file', required=True, type=click.Path(exists=True))
def print_sheet_json_auth(json_auth_file):
    """Print a small Google sheet. Requires a JSON authorization file."""
    gc = pygsheets.authorize(service_file=json_auth_file)
    sh = gc.open('biosamples-annotation-dg sample sheet')

    wks = sh[0]

    df = wks.get_as_df()

    print(df)


if __name__ == '__main__':
    print_sheet_json_auth()
