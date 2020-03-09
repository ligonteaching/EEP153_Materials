import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def read_sheets(key,json_creds=None,sheet=None):
    """Read google sheet having key/url 'key'.  

    If sheet is not public, supply a =json= filename for "service
    account" credentials (see
    https://gspread.readthedocs.io/en/latest/oauth2.html).

    Final argument identifies a particular "sheet" in the "workbook".
    This can be an integer or a string.
 
    Ethan Ligon                                         January 2020

    """

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    if json_creds is not None:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_creds,scope)
        gc = gspread.authorize(credentials)

    if 'https://' in key[:9]:
        wkb = gc.open_by_url(key)
    else:
        wkb = gc.open_by_key(key)

    if sheet is None:
        wks = wkb.worksheets()
        D={}
        for w in wks:
            data = w.get_all_values()
            headers = data.pop(0)
            df = pd.DataFrame(data, columns=headers)
            D[w.title]=df.apply(lambda x: pd.to_numeric(x,errors='ignore'))

        return D
    else: 
        try:
            wks = wkb.get_worksheet(int(sheet))
        except ValueError:
            wks = wkb.worksheet(sheet)
        data = wks.get_all_values()
        headers = data.pop(0)
        df = pd.DataFrame(data, columns=headers)

        return df.apply(lambda x: pd.to_numeric(x,errors='ignore'))
