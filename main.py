from flask import Flask, request, render_template, session, redirect, Response, url_for, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/problems')
def problems():
    return render_template('problems.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    app.run(host = '127.0.0.1', debug = True)