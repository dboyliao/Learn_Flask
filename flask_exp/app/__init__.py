from flask import Flask, request, render_template
from io import StringIO

app = Flask(__name__)

try:
    unicode(3)
except NameError:
    unicode = str

@app.route('/', methods = ['GET', 'POST'])
def all_data():
    body = request.stream.read()
    request.stream = StringIO(unicode(body))
    params = request.args
    form_data = request.form
    return render_template('show_params_data.html',
                           method = 'GET',
                           params = params,
                           form_data = form_data,
                           body = body)