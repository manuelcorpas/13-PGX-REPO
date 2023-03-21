import csv
import mariadb
import os
import re
import regex

try:
    db = mariadb.connect(host='localhost',user='admin',passwd='root',db='pgx')

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cursor = db.cursor(dictionary=True)

sql1 = "SELECT a.Gene,a.Drug,a.Alleles,s.Study_Cases,s.Biogeographical_Groups "  \
     + "FROM 01_var_drug_ann as a,00_study_parameters as s "                     \
     + "WHERE a.Variant_Annotation_ID = s.Variant_Annotation_ID"

sql2 = "INSERT INTO 02_var_drug_ann_study(Gene,Drug,Alleles,Study_Cases,Biogeographical_Groups) " \
     + "VALUES('{0}','{1}','{2}','{3}','{4}')"

cursor.execute(sql1)
results = cursor.fetchall()

for result in results:
    Gene                   = result['Gene']
    Drug                   = result['Drug']
    Alleles                = result['Alleles']
    Study_Cases            = result['Study_Cases']
    Biogeographical_Groups = result['Biogeographical_Groups']
    print(Gene,Drug,Alleles,Study_Cases,Biogeographical_Groups)
    cursor.execute(sql2.format(Gene,Drug,Alleles,Study_Cases,Biogeographical_Groups))
