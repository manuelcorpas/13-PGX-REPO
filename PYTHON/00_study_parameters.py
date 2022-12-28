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

sql1 = "INSERT INTO 00_study_parameters(Study_Parameters_ID,Variant_Annotation_ID"     \
     + ",Study_Type,Study_Cases,Study_Controls,Characteristics,Characteristics_Type"   \
     + ",Frequency_In_Cases,Allele_Of_Frequency_In_Cases,Frequency_In_Controls"        \
     + ",Allele_Of_Frequency_In_Controls,P_Value,Ratio_Stat_Type,Ratio_Stat"           \
     + ",Confidence_Interval_Start,Confidence_Interval_Stop,Biogeographical_Groups) "  \
     + "VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}'"     \
     + ",'{11}','{12}','{13}','{14}','{15}','{16}')"                      

os.chdir("INPUT/variantAnnotations")
myfile = "study_parameters.tsv"

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

