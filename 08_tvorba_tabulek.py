import pandas as pd
import numpy as np
import csv

pd.set_option('display.max_columns', None)

df_full = pd.read_csv("Sloupce_klicova_slova.csv", sep='\t', usecols=['ID vystupu', 'Organizace', 'Sociál', 'Činnost', 'Země', 'Lidé'])
df_full = df_full.rename(columns={'ID vystupu': 'ID_vystupu', 'Organizace': 'Organizace', 'Sociál': 'Zavinac', 'Činnost': 'Cinnost', 'Země': 'Zeme', 'Lidé': 'Lide'})

print(df_full.columns)


def create_table(df, key):
    df[key] = df[key].str.split(', ')
    df = df.explode(key)
    return df.to_csv(f'Tabulka_{key}.csv', encoding='utf-8', index=False)


df_organizace = df_full[["ID vystupu", "Organizace"]]
create_table(df_organizace, 'Organizace')

df_zavinac = df_full[["ID vystupu", "Zavinac"]]
create_table(df_zavinac, 'Zavinac')

df_cinnost = df_full[["ID vystupu", "Cinnost"]]
create_table(df_cinnost, 'Cinnost')

df_zeme = df_full[["ID vystupu", "Zeme"]]
create_table(df_zeme, 'Zeme')

df_lide = df_full[["ID vystupu", "Lide"]]
create_table(df_lide, 'Lide')
