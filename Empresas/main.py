from gsheet_pandas import DriveConnection
import pygsheets
import pandas as pd

import teste


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1SVmiZFf3gJ-ZOwtuZUw7UKZtyvognTdYk0BL_KcjTns"
SAMPLE_RANGE_NAME = "Página1!A1"


def main():
    gc = pygsheets.authorize(client_secret='credentials.json')
    spreadsheet_id = "1SVmiZFf3gJ-ZOwtuZUw7UKZtyvognTdYk0BL_KcjTns"
    sh = gc.open_by_key(spreadsheet_id)

    wks = sh[0]
    wks.set_dataframe(teste.tabela1, 'A1')

    wks = sh[1]
    wks.set_dataframe(teste.tabela2, 'A1')

    wks = sh[2]
    wks.set_dataframe(teste.tabela3, 'A1')

    wks = sh[3]
    wks.set_dataframe(teste.tabela4, 'A1')

    wks = sh[4]
    wks.set_dataframe(teste.tabela5, 'A1')

    wks = sh[5]
    wks.set_dataframe(teste.tabela6, 'A1')









if __name__ == "__main__":
  main()