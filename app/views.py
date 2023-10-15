from app import app
from flask import render_template, redirect, session, request

@app.route('/', methods=['GET', 'POST'])
def home():
    return "Hello, world!"