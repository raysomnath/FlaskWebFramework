from datetime import datetime
from flask import render_template
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    
    #html_content = "<html><head><title>Hello Flask</title></head><body>"
    #html_content += "<strong>Hello Flask!</strong> on " + formatted_now
    #html_content += "</body></html>"

    #return render_template("index.html", content = "<strong>Hello, Flask!</strong>" + formatted_now);

    return render_template(
        "index.html",
        title="Hello Flask",
        message = "Hello Flask!",
        content = " on " + formatted_now);

@app.route('/app/data')
def get_data():
    return app.send_static_file('data.json')

@app.route('/about')
def about():
    return render_template(
        "about.html",
        title= "About HelloFlask",
        content = "Example app page for Flask."
        )