import pandas as pd
import numpy as np
import re

# V tomto souboru nahrazuji substringy prázným řetězcem nebo zjednodušeným výrazem podle logiky,
# která vychází z naší kombinace seznamů kličových slov. Zároveň se zbavuji případných duplikátů vzniklých zjednodušováním.

df = pd.read_csv(r'C:\Users\Jarmila\Desktop\DA\Projekt\Jarmila_Cisteni_dat\Trideni.csv', sep='\t')

pd.set_option('max_colwidth', 120)

def clean_string(string):
        # Nahrazuji výrazy '@Člověk v Tísni' v kombinaci s dalším slovem (nenásleduje hend čárka), nechávám jen to další slovo:
        clean_string = re.sub(r'@Člověk v Tísni\s', '', string)
        # Nahrazuji výrazy 'Člověk v Tísni' v kombinaci s dalším slovem (nenásleduje hend čárka), nechávám jen to další slovo.
        # (Asi by se hodilo sloučit tyto dva řádky do jednoho, ale to mi nefunguje, zatím to nechávám být, takto to funguje výborně.)
        clean_string1 = re.sub(r'(?<!@)Člověk v Tísni\s', '', clean_string)
        # Ještě nahrazuji různé formulace názvu festivalu zjednodušeným výrazem "Jeden svět":
        clean_string2 = re.sub(r'Jeden svět Festival', 'Jeden svět', clean_string1)
        clean_string3 = re.sub(r'Festival Jeden svět', 'Jeden svět', clean_string2)
        # Ve zjednodušeném sloupci chceme mít unikátní hodnoty oddělené čárkou:
        clean_string4 = ','.join(set(clean_string3.split(', ')))
        final_clean_string = re.sub(r', Jeden svět', '', clean_string4)
        return final_clean_string.strip()


df['Klíčová slova'] = df['Klíčová slova'].apply(clean_string)

df.to_csv('Trideni_hotovo.csv', encoding='utf-8', sep='\t', index=False)
