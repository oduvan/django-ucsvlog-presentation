#легко читать и парсить
FORMAT = '''
"I1,","Call1,"Call2,"LOG,"Data1,"Data2
"I2,","Call1,"Call2,"LOG,"Data3,"Data4
"I3,"I1,"Call1,"Data2_2
"I4,"I1,"Call1,"Data1_2
'''

#легко писать
val = 'data'
val_ucsv = val.replace('"',
                       '""')