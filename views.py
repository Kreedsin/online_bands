from flask import Blueprint, render_template, request
from fav_bands import favourite_bands

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page2")
def page2():
    rating = request.args.get('rating')
    if rating:
        rating = int(rating)
        filtered_bands = [band for band in favourite_bands if band['rating'] == rating]
    else:
        filtered_bands = favourite_bands
    return render_template("page2.html", favourite_bands=filtered_bands)

@my_view.route("/my_name", methods=["GET", "POST"])
def my_name():
    if request.method == "POST":
        new_band = request.form["added_band"]
        song = request.form['favorite_song']
        album = request.form['favorite_album']
        rating = int(request.form['rating'])
        favourite_bands.append({
        'band': new_band,
        'song': song,
        'album': album,
        'rating': rating
    })

    return render_template("my_name.html")

# @my_view.route("/filtered, methods=["GET", "POST"])
# def filtered(rating):
#     filtered_bands = [band for band in favourite_bands if int(band['rating']) == rating]
#     return jsonify(filtered_bands)

@my_view.route('/ratings/<int:rating>', methods=['GET'])
def get_ratings(rating):
    filtered_bands = [band for band in favourite_bands if band['rating'] == rating]
    return (filtered_bands)