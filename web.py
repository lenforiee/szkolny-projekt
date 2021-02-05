from quart import Quart, render_template, request
import os

app = Quart(__name__)
__author__ = "Lenforiee"
__version__ = "1.0.0"

@app.errorhandler(404)
async def page_not_found(e):
    """Our own custom 404 page"""

    return await render_template('homepage.html'), 404

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    app.run(debug=True) # blocking call