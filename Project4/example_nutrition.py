#%pip install -r hackingfood_requirements.txt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cfe.regression as rgsn

Uganda_Data = '1yFWlP5N7Aowaj6t2roRSFFUC50aFD-RLBGfzGtqLl0w'

from ligonlibrary.sheets import read_sheets

# Change 'Uganda_Data' to key of your own sheet in Sheets, above
x = read_sheets(Uganda_Data,sheet='Food Expenditures (2019-20)')
x = x.set_index(['i','t','m','j']).squeeze()


# Now prices
p = read_sheets(Uganda_Data,sheet='Food Prices (2019-20)').set_index(['t','m','j','u'])

# Compute medians of prices for particular time, place and unit
p = p.groupby(['t','m','j','u']).median()

# Just keep metric units
p = p.xs('Kg',level="u").squeeze().unstack('j')

# Get intersection of goods we have prices *and* expenditures for:
jidx = p.columns.intersection(x.index.levels[-1])

# Drop prices for goods we don't have expenditures for
p = p[jidx].T

# Household characteristics
d = read_sheets(Uganda_Data,sheet="Household Characteristics")
d.columns.name = 'k'

# Fill blanks with zeros
d = d.replace(np.nan,0)

# Expenditures x may have duplicate columns
x = x.groupby(['i','t','m','j']).sum()
x = x.replace(0,np.nan) # Replace zeros with missing

# Take logs of expenditures; call this y
y = np.log(x)

d.set_index(['i','t','m'],inplace=True)

r = rgsn.Regression(y=y,d=d)

# Assumes you've already set this up e.g., in Project 3
# r = rgsn.read_pickle('../Project3/uganda_estimates.rgsn')

fct = read_sheets(Uganda_Data,sheet='FCT')

fct = fct.set_index('j')
fct.columns.name = 'n'

fct = fct.apply(lambda x: pd.to_numeric(x,errors='coerce'))

rdi = read_sheets(Uganda_Data,sheet='RDI')

rdi = rdi.set_index('n')
rdi.columns.name = 'k'

rdi = rdi.apply(lambda x: pd.to_numeric(x,errors='coerce'))

# Reference prices chosen from a particular time; average across place.
# These are prices per kilogram:
# NB: fillna(1) replaces missing prices with 1 (currency unit per kg).
# This is a rough default so that the code runs; in a serious analysis
# you would want to investigate *which* goods lack price data and
# either find prices from another source or drop those goods.
pbar = p.loc[r.get_beta().index].mean(axis=1).fillna(1)

xhat = r.predicted_expenditures()

# Total food expenditures per household
xbar = xhat.groupby(['i','t','m']).sum()

# Reference budget
xref = xbar.quantile(0.5)  # Household at 0.5 quantile is median

qhat = (xhat.unstack('j')/pbar).dropna(how='all')

# Drop missing columns
qhat = qhat.loc[:,qhat.count()>0]

qhat

def ceteris_paribus_price(j,p0,p=pbar):
    """
    Return price vector with the price of good j set to p0,
    holding all other prices fixed at p.
    """
    p = p.copy()
    p.loc[j] = p0
    return p

fct

# Create a new FCT and vector of consumption that only share rows in common:
fct0,c0 = fct.align(qhat.T,axis=0,join='inner')
print(fct0.index)

# The @ operator means matrix multiply
N = fct0.T@c0

N  #NB: Uganda quantities are for previous 7 days

def nutrient_demand(x,p,r=r,fct=fct):
    c = r.demands(x,p)
    fct0,c0 = fct.align(c,axis=0,join='inner')
    N = fct0.T@c0

    # Drop duplicate nutrient rows (keeps first).  If your FCT has
    # duplicates this silently discards data; worth checking with
    # fct.index[fct.index.duplicated()] to see what's being dropped.
    N = N.loc[~N.index.duplicated()]

    return N

# In first round, averaged over households and villages
dbar = r.d[rdi.columns].mean()

# This matrix product gives minimum nutrient requirements for
# the average household
hh_rdi = rdi@dbar

hh_rdi

def nutrient_adequacy_ratio(x,p,d,rdi=rdi,days=7):
    hh_rdi = rdi.replace('',0)@d*days

    return nutrient_demand(x,p)/hh_rdi
