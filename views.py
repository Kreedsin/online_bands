from flask import Blueprint, render_template, request
from fav_bands import favourite_bands

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page2")
def page2():
    return render_template("page2.html", favourite_bands = favourite_bands)

@my_view.route("/my_name", methods=["GET", "POST"])
def my_name():
    if request.method == "POST":
        new_band = request.form["added_band"]
        song = request.form['favorite_song']
        album = request.form['favorite_album']
        rating = request.form['rating']
        favourite_bands.append({
        'band': new_band,
        'song': song,
        'album': album,
        'rating': rating
    })

    return render_template("my_name.html")