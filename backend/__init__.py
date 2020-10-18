from flask import Flask, render_template, send_from_directory
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='../dist/static', template_folder='../dist')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)

from backend.api import test_bp
app.register_blueprint(test_bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, '../dist/static/img'), 'favicon.ico', )

