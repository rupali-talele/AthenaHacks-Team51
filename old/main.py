#!/usr/bin/env python
import os
import urllib.parse 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# Configure Database URI: 
params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=athenahacks.database.windows.net;DATABASE=athenahacks ;UID=azureuser;PWD=athenahacks!")

# DRIVER={ODBC Driver 17 for SQL Server};SERVER=athenahacks.database.windows.net;DATABASE=athenahacks ;UID=azureuser;PWD=athenahacks!

# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# extensions
db = SQLAlchemy(app)