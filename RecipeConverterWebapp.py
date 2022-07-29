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
add_to_table_grams=tuple(c.fetchall())
#data from mills table
c.execute("SELECT * FROM militres")
add_to_table_mills=tuple(c.fetchall())

#Recipe converter
conversion_to_grams_dict = {'ounce':28.35,
                      'pound':454,
                      'stick':113}

conversion_to_mills_dict = {'cup':240,
                      'teaspoon':5,
                      'tablespoon':15,
                       'pint':473,
                       'quart':946}

#Function to convert measurements into mills
def conversion_to_mills(measure,num_measure):
    return conversion_mills[measure.lower()]*num_measure


#Function to convert measurement to grams
def conversion_to_grams(measure,num_measure):
    return conversion_grams[measure.lower()]*num_measure



#Headings for table
heading_table_grams=('Measurement','Number of measurement','Conversion to grams')
heading_table_mills=('Measurement','Number of measurement','Conversion to mills')


#Flask app code
app = Flask(__name__)
app.config['SECRET_KEY'] ='''uOY TRUH DNa EIl A LLet aNnOG revEN
EyBdoOg YaS AnNOG rEVEn
YrC uoy eKAm AnnoG rEVEn
UOy treSeD DnA dNUorA NUR ANnOg REveN
NWOD uoY TEL ANNog ReVeN
PU UOy Evig aNNOg reVen
UOy tRuH DNA eIl A LLeT AnNog REVEN
EybdOOG YAs AnnOg revEn
yrc UOY EkAM AnNOG REveN
Uoy trEsEd DNA dNUoRA nUr annOg ReVen
NWOd uOY TEL aNNoG rEvEN
PU uoY eviG aNnog REven
UoY truH dNA Eil A lleT aNNOG ReVEn
EYBDOOG yaS annOg ReVEn
Yrc UoY eKaM ANNog REveN
uoY TREsEd DNA dNUORa NUr aNnOg ReVEN
Nwod Uoy TEl aNNOG reVen
pU UOy eVIG anNOg reVEN
dnatSREDnU uOy EKam ATtoG
gNiLeEF m'i WOh uOY lLeT ANnaW tSUj I
tI YalP AnnOg er'Ew dNa eMAg eHT WoNk Ew
)no GNiog( no GnIog Neeb s'TAHW woNk htOb eW ,ediSNi
)ti yas OT( tI YaS oT yHs Oot Er'uOy TuB ,gNihca neeB S'TraEH RUoy
gNoL os ROf RehTo hcae NWOnk eV'ew
uoy TRUh DNA Eil a lLEt annog REvEN
eYBdOOG yaS aNnOG rEven
yrc uOy eKAm ANNOG revEn
UOy treSED DNA DnUoRA Nur AnnOg REVen
NwOd uoy tel ANnOG REveN
pU uoy eVIG ANNoG REVen
Uoy tRuh DnA EIl a lLeT ANnOG reVen
eybDooG yAs ANNOG rEVeN
YrC uOy Ekam AnNOG reven
uoy tReSed DNA dnuorA NUR aNnOg RevEN
NwoD UOy TEL aNnog reven
pU Uoy evIg aNnOg RevEn
eeS oT dnILb oot er'uoY em LlEt t'nOD
GNilEEf m'i WOh EM ksa uoY FI dnA
ti yAlp aNNOG er'eW dNa EmaG Eht wOnK eW
)NO gNioG( nO Gniog NEeb S'TaHw WoNK Htob ew ,EDisNI
)TI YAS( TI YAs OT YhS oOT Er'UOY tUB ,GNIhcA NeEb S'TrAeH ruOY
gnOL OS rOF ReHTO hcae NwonK EV'eW
UOY TRuH DNA eIL A LLEt ANNOG reVeN
EYBdOog YAS annOg rEVEN
yRc uOY eKAm aNnOG ReVen
UoY tREsed dna dnUOra nUr anNOG reven
NWod UoY TEl aNnoG REVeN
Pu uOy EVIg Annog ReVen
dnatSrEDnU UoY eKam atTog
GNiLeEF m'i wOH UoY LLET ANnAw tSUJ I
YUG Rehto yna morF SIHT teg t'NdLuOW uOY
fO GNiKnIhT M'i tAhw s'tneMTiMmOc LLuf a
)i oD( I Od OS DNa seLUR EhT WOnK UOY
eVOL OT sregNaRtS On Er'ew'''
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
            conversion=conversion_to_mills(measurement_mills,number_measurements)
            add_to_table_mills=(measurement_mills,number_measurements,conversion)
            c.execute("INSERT INTO militres VALUES(?,?,?)",add_to_table_mills)
        else:
            measurement_grams=request.form['unitgrams']
            number_measurements=request.form['numberofunits']
            conversion=conversion_to_grams(measurement_grams,number_measurements)
            add_to_table_grams=(measurement_mills,number_measurements,conversion)
            c.execute("INSERT INTO militres VALUES(?,?,?)",add_to_table_grams)
            return render_template('conversion.html')
            
    else:
        return render_template('conversions.html',)
    


@app.route("/conversionmills")
def conversion_mills():
    return render_template('conversion_mill.html',heading_table_mills=heading_table_mills, add_to_table_mills=add_to_table_mills)


@app.route("/conversiongrams")
def conversion_grams():
    return render_template('conversion_grams.html',heading_table_grams=heading_table_grams,add_to_table_grams=add_to_table_grams)    

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/testform")
def testform():
    return render_template('testform.html')
app.run(debug=True)

