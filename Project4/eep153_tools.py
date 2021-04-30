import gspread
from google.oauth2.service_account import Credentials
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

    try: # key may be dict indexed by sheet
        key = key[sheet]
    except TypeError: # not a dict?
        pass

    if json_creds is not None:
        credentials = Credentials.from_service_account_file(json_creds,scopes=scope)
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

import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from gspread_pandas import Client, Spread
from gspread_pandas.client import SpreadsheetNotFound

def write_sheet(df,user_email,user_role='reader',json_creds=None,key='',sheet='My Sheet'):
    """Write df to google sheet having =key= and sheet name =sheet=.
 
    Alternatively, key may be a title for the spreadsheet.

    If sheet is not public, supply a =json= filename for "service
    account" credentials (see
    https://gspread.readthedocs.io/en/latest/oauth2.html).

    Final argument identifies a particular "sheet" in the "workbook".
    This can be an integer or a string.
 
    Ethan Ligon                                         April 2021
    """

    if "http" in key and "/" in key: # Deal with case of a url
        url = key
        bits = url.split('/')
        key = bits[bits.index('d')+1]

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = Credentials.from_service_account_file(json_creds,scopes=scope)
    client = gspread.authorize(credentials)

    try:
        spread = Spread(key,client=client)
        id = key
    except SpreadsheetNotFound:
        s = client.create(key)
        id = s.id
        spread = Spread(id,client=client)
        spread.delete_sheet('Sheet1')

    client.insert_permission(id,user_email,perm_type='user',role=user_role)

    spread.df_to_sheet(df,sheet=sheet)        

    return id
