# Chystam se rozdelit sloupec klicovych slov podle kategorii definovanych jednotlivymi seznamy.

# Pisu si funkci, kterou pouziju v ramci cteni a zapisu souboru .csv.
# Funkce keywords_into_column:
# 1. Dostane seznam klicovych slov a v cyklu projde kazdy radek souboru krome headers. Zkontroluje, ktera z klicovych
# slov dany radek obsahuje a vlozi je do nove vznikleho sloupce podle kategorie klicovych slov z prijateho seznamu.
# 2. Pokud slovo z daneho seznamu nenajde, vlozi do sloupce 'NaN'.
# 3. Odstrani toto klicove slovo z kontrolniho seznamu klicovych slov pro dany radek. 
# 
# Cilem je mit ve vyslednem .csv souboru:
# 1. Puvodni sloupec 'ID vystupu'
# 1. Puvodni Sloupec 'Klicova slova', kde zustavaji stringy vsech neroztridenych klicovych slov. 
# 2. Kontrolni sloupec 'Keywords_test', ktery by mel po ukonceni programu zustat cely prazdny za podminky, 
#    ze se v datasetu objevila vsechna klicova slova.
# 3. Dale budou nasledovat sloupce 'Organizace', 'Social', 'Cinnost', 'Zeme' a 'Lide', 
#    ve kterych bude vzdy retezec klicovych slov (oddelenych carkou) podle kategorie.

def keywords_into_column(keywords_list):
        words_appended = 0
        keywords_column = [] # Sloupec, do kterého se zapíší všechna klíčová slova z dané kategorie
        keywords_test = line[2] # Kontrolní sloupec, který má na konci zůstat prázdný.
        for word in keywords_list:
            if word in klicova_slova_list:
                words_appended  += 1
                if words_appended == 1:
                    keywords_column.append(word)
                if words_appended > 1:
                    keywords_column.append(word)
                if word in keywords_test:
                    keywords_test.remove(word) # Odstraní připsané slovo z kontrolního sloupce.
        if not keywords_column:
            keywords_column = 'NaN'
        line.append(str(keywords_column)) # Při čtení a zápisu souboru vytvoří nový sloupec pro danou kategorii klíčových slov.


organizace = [  'Člověk v Tísni',
                'ADRA', 
                'Amnesty International',
                'Charita',
                'Červený kříž',
                'Dobrý Anděl',
                'Greenpeace',
                'Lékaři bez hranic',
                'UNICEF'
            ]

social =  [ '@Člověk v Tísni',
            '@ADRA', 
            '@Amnesty International',
            '@Charita',
            '@Červený kříž',
            '@Dobrý Anděl',
            '@Greenpeace',
            '@Lékaři bez hranic',
            '@UNICEF'
        ]

cinnost = [ 
            'Humanitární pomoc',
            'Rozvojová spolupráce', 
            'Sociální bydlení', 
            'Sociální práce', 
            'Aktivismus',
            'Dobrovolnictví', 
            'Boj proti chudobě', 
            'Pomoc uprchlíkům', 
            'Ukrajina', 
            'Lidská práva', 
            'Vzdělávání v rozvojových zemích',
            'Občanská společnost',
            'Doučování',
            'Studentské volby',
            'Volby nanečisto',
            'Vzdělávací program varianty', 
            'Festival Jeden+svět',
            'Paměť národa',
            'Skutečný dárek',
            'Dluhy',
            'Exekuce',
            'Retrostipendia',
            'Mediální gramostnost',
            'Mediální výchova',
            'Jeden svět'
        ]
# Jeden svět zahrnut v činnostech

zeme = [
        'AFGHÁNISTÁN', 
        'ANGOLA', 
        'ARMÉNIE', 
        'ÁZERBÁJDŽÁN', 
        'BARMA', 
        'MYANMAR', 
        'BĚLORUSKO', 
        'BOSNA HERZEGOVINA', 
        'ČESKÁ REPUBLIKA', 
        'KONGO', 
        'EGYPT', 
        'EKVÁDOR', 
        'ETIOPIE', 
        'FILIPÍNY', 
        'GRUZIE', 
        'HONDURAS', 
        'IRÁK', 
        'JEMEN', 
        'KAMBODŽA', 
        'KOSOVO', 
        'KUBA', 
        'LIBYE', 
        'Mali', 
        'MOLDAVSKO', 
        'MONGOLSKO', 
        'NEPÁL', 
        'NIKARAGUA', 
        'PODNĚSTŘÍ', 
        'RUMUNSKO', 
        'MAKEDONIE', 
        'SRBSKO', 
        'STŘEDNÍ ASIE', 
        'SÝRIE', 
        'TURECKO', 
        'UKRAJINA', 
        'VENEZUELA', 
        'VIETNAM', 
        'ZAMBIE'
        ]

lide = [
        'Šimon Pánek', 
        'Daniel Hůle', 
        'Tomáš Vyhnálek', 
        'Tomáš Urban', 
        'Denisa Bultasová', 
        'Jan Mrkvička', 
        'Tomáš Habart', 
        'Karel Strachota', 
        'Ondřej Kamenický', 
        'Tomáš Kocian',
        'Ivo Dokoupil',
        'Dušan Pořízek',
        'Jitka Trachtová'
        ]


with open(r'C:\Users\Jarmila\Desktop\DA\Projekt\Df_klicova_slova_zjednoduseno_2.csv', mode='r', encoding='utf-8') as input_file:
    with open('Sloupce_klicovych_slov.csv', mode='w', encoding='utf-8') as output_file:
        text_input = input_file.readlines()
        text_output = []
        headers = text_input[0].strip().split('\t')
        headers.append('Keywords_test')
        headers.append('Organizace')
        headers.append('Social')
        headers.append('Cinnost')
        headers.append('Zeme')
        headers.append('Lide')
        headers = '\t'.join(headers) + '\n'
        text_output.append(headers)
        for line in text_input[1:]:
            line = line.strip().split('\t')
            id_vystupu, klicova_slova = line
            klicova_slova_list = klicova_slova.split(',')
            line.append(klicova_slova_list)
            keywords_into_column(organizace)
            keywords_into_column(social)
            keywords_into_column(cinnost)
            keywords_into_column(zeme)
            keywords_into_column(lide)
            line[2] = str(line[2])
            line = '\t'.join(line) + '\n'
            line = line.replace('[', '')
            line = line.replace(']', '')
            line = line.replace("'", "")
            text_output.append(line)
        output_file.writelines(text_output)