#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
$ python scripts/plot.py
$ python scripts/plot.py --country France --currency Euro --indicator "Gross Domestic Product (GDP)"
"""

import click

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@click.command()
@click.option('--data', default="data/gdp_by_industry_and_country.csv", help=u"Filename")
@click.option('--country', default="France", help=u"Country")
@click.option('--currency', default="Euro", help=u"Currency")
@click.option('--indicator', default="Gross Domestic Product (GDP)", help=u"Indicator Name")
def main(data, country, currency, indicator):
    df = pd.read_csv(data)
    df = df.set_index(['Country', 'Currency', 'IndicatorName'])
    df = df.transpose()
    df.index = df.index.astype(int)
    #df.index = df.index.map(lambda y: datetime.date(year=int(y), month=1, day=1))
    ts = df[country][currency][indicator]
    ts = ts.str.replace(',', '').astype(np.long)
    ts.plot()
    plt.show()

if __name__ == '__main__':
    main()
