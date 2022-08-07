from flask import Flask,render_template,redirect,request
import sqlite3

#Database 
connect=sqlite3.connect('Conversion')
c=connect.cursor()
#Intial setup of database

try:
    #Create table to store measurement entered in mills
    c.execute("CREATE TABLE militres(unit TEXT,number_of_unit INTERGER,conversion INTERGER)")
    #Create table to store measurement entered in grams
    c.execute("CREATE TABLE grams(unit TEXR,number of unit number,conversion number)")
    print("Database Setup")
    connect.close()
    connect.commit()
except:
    pass

finally:
    print("Database connected")

#Get data from tables in database
#Query data from grams table in conversions Database
try:
    c.execute("SELECT * FROM grams")
    DisplaytoTableGrams=tuple(c.fetchall())
    print("Data queried from Table grams")
except:
    pass
#data from mills table
try:
    c.execute("SELECT * FROM militres")
    DisplaytoTableMills=tuple(c.fetchall())
    print("Data queried from Table Mills")
except:
    pass
#Recipe converter
conversion_to_grams_dict = {'ounce':28.35,
                      'pound':454,
                      'stick':113}
#Dictionary to convert form input from user into equivalent in grams. 
conversion_to_mills_dict = {'cup':240,
                      'teaspoon':5,
                      'tablespoon':15,
                       'pint':473,
                       'quart':946}
#Dictionary to convert form input from user into equivalent in mills. 
#Units
unit_to_grams=('ounce','pound','stick')
unit_to_mills=('teaspoon','tablespoon','cup','quart','pint')

#Headings for table
heading_table_grams=('Number of measurement','Measurement','Conversion to grams')
heading_table_mills=('Number of measurement','Measurement','Conversion to militres')


#Flask app code
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/convert')
def converter():
    return render_template('convert.html',units_grams=unit_to_grams,units_mills=unit_to_mills)

  
@app.route("/conversions/", methods=['POST','GET'])
def conversions():
    if request.method=='POST':
        millsorgrams=request.form['Militres or Grams']
        if millsorgrams == 'Militres':
            measurement_mills=request.form['unitmills']
            # This gets the measurement that the user has selected from the form
            print(measurement_mills)
            #Print statement to check what the measurement is. 
            number_measurements=float(request.form['numberofunits'])
             # This gets the number of measure that the user has enter in the form
            print(number_measurements)
            # Print statment to check what number is 
            conversion_mills=float(conversion_to_mills_dict[measurement_mills])*float(number_measurements) 
            #This gets the usermeasurement from the form and then converts it into mills using it as a key in a dictionary. This is then multiplied by the number of measurements to get the final conversion. 
            print(conversion_mills)  
            #Print conversion to see if it is correct.      
            add_to_tale_mills=(measurement_mills,number_measurements,conversion_mills)
            #This is tuple which will be inserted into the Database.  
            print(add_to_tale_mills)
            # See if it is correct. 
            connect=sqlite3.connect('Conversion')
            c=connect.cursor()
            c.execute("INSERT INTO militres VALUES(?,?,?)",add_to_tale_mills)
            # Inserts form data into database. 
            connect.commit()
            connect.close()
            return render_template('conversions.html')
        else:
            measurement_grams=request.form['unitgrams']
            print(measurement_grams)
            number_measurements=request.form['numberofunits']
            print(number_measurements)
            conversion_grams=float(conversion_to_grams_dict[measurement_grams])*float(number_measurements) 
            #This gets the usermeasurement from the form and then converts it into grams using it as a key in a dictionary. This is then multiplied by the number of measurements to get the final conversion. 
            print(conversion_grams)
             #Print conversion to see if it is correct.      
            add_to_tale_grams=(measurement_grams,number_measurements,conversion_grams)
            #This is tuple which will be inserted into the Database.
            print(add_to_tale_grams)
            connect=sqlite3.connect('Conversion')
            c=connect.cursor()
            c.execute("INSERT INTO grams VALUES(?,?,?)",add_to_tale_grams)
            # Inserts form data into database.
            connect.commit()
            connect.close()
            return render_template('conversions.html')
            
    else:
        return render_template('conversions.html',)
    


@app.route("/conversionmills")
def conversion_mills():
    connect=sqlite3.connect('Conversion')
    c=connect.cursor()
    c.execute("SELECT * FROM militres")
    #Gets all data crom militres table
    add_to_table_mills=tuple(c.fetchall())
    return render_template('conversion_mill.html',heading_table_mills=heading_table_mills, add_to_table_mills=add_to_table_mills)


@app.route("/conversiongrams")
def conversion_grams():
    connect=sqlite3.connect('Conversion')
    c=connect.cursor()
    c.execute("SELECT * FROM grams")
    add_to_table_grams=tuple(c.fetchall())
    return render_template('conversion_grams.html',heading_table_grams=heading_table_grams,add_to_table_grams=add_to_table_grams)    

app.run(debug=True)

