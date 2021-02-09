from quart import Quart, render_template, request
import os

app = Quart(__name__)
__author__ = "Lenforiee"
__version__ = "1.0.0"

@app.route("/")
async def home_page():
    """Render strony głownej."""

    return await render_template('homepage.html')

@app.route("/browse")
async def browse():
    """Render strony głownej."""

    return await render_template('browse.html')

@app.errorhandler(404)
async def page_not_found(e):
    """Nasz własny 404 error handler."""

    return await render_template('404.html'), 404

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    app.run(debug=True)