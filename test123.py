from flask import Flask, render_template
import sqlite3
app = Flask(__name__)



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/conversion')
def conversion():
    return ('conversions.html')
@app.route('/converter')
def converter():
	return render_template('convert.html')

@app.route('/conversionmills')
def conversionmills():
	return render_template('conversionmills.html')



app.run(debug=True)
