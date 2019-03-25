import os
from flask import Flask, render_template, flash
from content_management import Content
app = Flask(__name__)

TOPIC_DICT = Content()

app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def homepage():
	return render_template('main.html')

@app.route('/dashboard/')
def dashboard():
	flash('Hola Amigo')
	return render_template('dashboard.html', TOPIC_DICT = TOPIC_DICT)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')
if __name__ == "__main__":
	app.run()