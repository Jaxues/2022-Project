from datetime import date
import sqlite3

units=('ounce','pound','stick','teaspoon','tablespoon','cup','quart','pint')

units_grams=('ounce',
'pound',
'stick')
units_mills=('teaspoon',
'tablespoon',
'cup',
'quart',
'pint')
conversion_to_grams = {'ounce':28.35,
                      'pound':454,
                      'stick':113}

conversion_to_mills = {'cup':240,
                      'teaspoon':5,
                      'tablespoon':15,
                       'pint':473,
                       'quart':946}


#Intinually create table in database. 
connect=sqlite3.connect('Conversion')
c=connect.cursor()


#


list_mills=[]
list_grams=[]


numbers=[1,2,3]
numbers_mills=[1,2,3,4,5]
x=0
while x ==1:
    x+=1
    for (measure,number) in zip(units_mills,numbers_mills):
            date=date.today()
            final_conversion_mills=conversion_to_mills[measure.lower()]*number
            add_to_table=(measure,number,final_conversion_mills)
            list_mills.append(add_to_table)
    for (measure,number) in zip(units_grams,numbers):
            date=date.today()
            final_conversion_grams=conversion_to_grams[measure.lower()]*number
            add_to_table=(measure,number,final_conversion_grams)
            list_grams.append(add_to_table)
    print("comnand executed change x please.")

c.executemany("INSERT INTO grams VALUES (?,?,?)",list_grams)
c.executemany("INSERT INTO militres VALUES (?,?,?)",list_mills)
connect.commit()
    

c.execute("SELECT * FROM grams")
add_to_table_grams=tuple(c.fetchall())
print(add_to_table_grams)
