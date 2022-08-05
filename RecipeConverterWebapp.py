from flask import Flask,render_template,redirect,request
import sqlite3
import datetime
from Data import units_mills,units_grams

#Database 
#Create table to store measurement entered in mills
connect=sqlite3.connect('Conversion')
c=connect.cursor()

try:
    c.execute("CREATE TABLE militres(unit text,number of unit number,conversion number)")
except:
    pass

#Create table to store measurement entered in grams
try:
    c.execute("CREATE TABLE grams(unit text,number of unit number,conversion number)")
except:
    pass



#Get data from tables in database
#data from grams table
c.execute("SELECT * FROM grams")
DisplaytoTableGrams=tuple(c.fetchall())
#data from mills table
c.execute("SELECT * FROM militres")
DisplaytoTableMills=tuple(c.fetchall())

#Recipe converter
conversion_to_grams_dict = {'ounce':28.35,
                      'pound':454,
                      'stick':113}

conversion_to_mills_dict = {'cup':240,
                      'teaspoon':5,
                      'tablespoon':15,
                       'pint':473,
                       'quart':946}

#Headings for table
heading_table_grams=('Measurement','Number of measurement','Conversion to grams')
heading_table_mills=('Measurement','Number of measurement','Conversion to mills')


#Flask app code
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/convert')
def converter():
    return render_template('convert.html',units_grams=units_grams,units_mills=units_mills)

  
@app.route("/conversions/", methods=['POST','GET'])
def conversions():
    if request.method=='POST':
        millsorgrams=request.form['Militres or Grams']
        if millsorgrams == 'Militres':
            measurement_mills=request.form['unitmills']
            number_measurements=request.form['numberofunits']
            conversion_mills=conversion_to_mills_dict[measurement_mills]*number_measurements            
            add_to_tale_mills=(measurement_mills,number_measurements,conversion_mills)
            connect=sqlite3.connect('Conversion')
            c=connect.cursor()
            c.execute("INSERT INTO militres VALUES(?,?,?)",add_to_tale_mills)
            connect.commit()
            connect.close()
            return render_template('conversions.html')
        else:
            measurement_grams=request.form['unitgrams']
            number_measurements=request.form['numberofunits']
            conversion_grams=conversion_to_grams_dict[measurement_grams]*number_measurements
            add_to_tale_grams=(measurement_grams,number_measurements,conversion_grams)
            connect=sqlite3.connect('Conversion')
            c=connect.cursor()
            c.execute("INSERT INTO grams VALUES(?,?,?)",add_to_tale_grams)
            connect.commit()
            connect.close()
            return render_template('conversions.html')
            
    else:
        return render_template('conversions.html',)
    


@app.route("/conversionmills")
def conversion_mills():
    connect=sqlite3.connect('Conversion')
    c=connect.cursor()
    c.execute("Select * FROM militres")
    add_to_table_mills=tuple(c.fetchall())
    return render_template('conversion_mill.html',heading_table_mills=heading_table_mills, add_to_table_mills=add_to_table_mills)


@app.route("/conversiongrams")
def conversion_grams():
    connect=sqlite3.connect('Conversion')
    c=connect.cursor()
    c.execute("SELECT * FROM grams")
    add_to_table_grams=tuple(c.fetchall())
    return render_template('conversion_grams.html',heading_table_grams=heading_table_grams,add_to_table_grams=add_to_table_grams)    

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/testform")
def testform():
    return render_template('testform.html')
app.run(debug=True)

