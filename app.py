from flask import Flask
from flask import render_template
from flask import request 
from database import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/', methods=['GET', 'POST'])

def catbook_home():
	cats = get_all_cats()
	if request.method == 'GET':
		return render_template('home.html',cats = cats)
	else : 
		name = request.form['firstname']
		last_name = request.form['lastname']
		cat = ad(name)
		return render_template("actually_add_cat.html", cat = cat)



@app.route('/cats/<int:id>')
def cat_page(id):
	cat = get_one_cat(id)
	return render_template('cat.html', cat = cat )

@app.route('/add')
def actually_add_cat():
	return render_template("add_cat.html")

if __name__ == '__main__':
   app.run(debug = True)
