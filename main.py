from flask import Flask, render_template, send_file


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    if page_name == 'manifest.webmanifest':
        return send_file('manifest.webmanifest')
    elif page_name == 'cv.pdf':
        return send_file('static/cv/cv.pdf')
    else:
        return render_template(page_name)
