import mariadb
import re

try:
    db = mariadb.connect(host='localhost',user='admin',passwd='root',db='pgx')

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cursor = db.cursor(dictionary=True)

sql1 = "SELECT Study_Cases,Biogeographical_Groups "  \
     + "FROM 02_var_drug_ann_study "                 \

cursor.execute(sql1)
results = cursor.fetchall()

group_dict = {}

for result in results:
    Cases  = result['Study_Cases']
    Groups = result['Biogeographical_Groups']
    if not Cases:
        Cases = 0
    if re.search("Multiple groups",Groups):
        if not 'Multiple groups' in group_dict:
            group_dict['Multiple groups'] = 0
        else:
            group_dict['Multiple groups'] += int(Cases)
    elif re.search("Custom",Groups):
        if not 'Custom' in group_dict:
            group_dict['Custom'] = 0
        else:
            group_dict['Custom'] += int(Cases)
    elif Groups == '':
        if not 'No group' in group_dict:
            group_dict['No group'] = 0
        else:
            group_dict['No group'] += int(Cases)
    else:
        if not Groups in group_dict:
            group_dict[Groups] = 0
        else:
            group_dict[Groups] += int(Cases)
for key in group_dict:
    print(','.join(str(bit) for bit in [key,group_dict[key]]))
#    cursor.execute(sql2.format(Gene,Drug,Alleles,Study_Cases,Biogeographical_Groups))
