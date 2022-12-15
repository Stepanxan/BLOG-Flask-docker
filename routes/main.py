from app import app
from flask import render_template, url_for
from flask_login import login_required
from models.models import Posts



@app.route('/')
def index():
    print( url_for('index'))
    return render_template("index.html")


@app.route('/about')
@login_required
def about():
    print(url_for('about'))
    return render_template("about.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_404.html'),404


@app.route("/post:<post_id>")
def post_detail_main(post_id):
    detail = Posts.query.get(post_id)
    return render_template("post_detail_main.html", detail=detail)
