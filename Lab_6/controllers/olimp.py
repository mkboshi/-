import constants
from app import app
from flask import render_template, request
@app.route('/olimp/<ol>')
def olimp(ol):
    html = render_template(
    'olimp.html',
    ol = ol,
    discription = constants.olimp_dict[ol]
    )
    return html
