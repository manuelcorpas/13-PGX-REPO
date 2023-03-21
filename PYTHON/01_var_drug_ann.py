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

sql1 = "INSERT INTO 01_var_drug_ann(Variant_Annotation_ID"          \
     + ",Variant_Haplotypes,Gene,Drug,PMID,Phenotype_Category"      \
     + ",Significance,Notes,Sentence,Alleles,Specialty_Population)" \
     + " VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')"     

os.chdir("INPUT/variantAnnotations")
myfile = "var_drug_ann.tsv"

with open(myfile) as f:
    reader = csv.reader(f,delimiter="\t")
    next(reader, None)
    for row in reader:
        print(row)
        # replace single quotes
        my_line = [i.replace("'", " ") for i in row]
        # replace non latin characters
        out_line = []
        for text in my_line:
            stripped_text = ''
            for c in text:
                stripped_text += c if len(c.encode(encoding='utf_8'))==1 else ''
            out_line.append(stripped_text)
        cursor.execute(sql1.format(*out_line))

