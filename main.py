from flask import Flask, request, render_template, session, redirect, Response, url_for, send_file

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/data')
def data_page():
    return render_template('data.html')

@app.route('/problems')
def problems_page():
    problems = [
        {'lc_link': 'https://leetcode.com/problems/3sum/',
         'sol_link': '',
         'name': '3Sum',
         'company': 'paypal',
         'number': 15,
         'difficulty': 'Medium',
         'topics': 'Array, Two Pointers, Sorting'},
        {'lc_link': 'https://leetcode.com/problems/multiply-strings/',
         'sol_link': '',
         'name': 'Multiply Strings',
         'company': 'microsoft',
         'number': 43,
         'difficulty': 'Medium',
         'topics': 'Math, String, Simulation'},
        {'lc_link': 'https://leetcode.com/problems/group-anagrams/',
         'sol_link': '',
         'name': 'Group Anagrams',
         'company': 'amazon',
         'number': 49,
         'difficulty': 'Medium',
         'topics': 'Hash Table, String, Sorting'},
        {'lc_link': 'https://leetcode.com/problems/powx-n/',
         'sol_link': '',
         'name': 'Pow(x, n)',
         'company': 'amazon',
         'number': 50,
         'difficulty': 'Medium',
         'topics': 'Math, Recursion'},
        {'lc_link': 'https://leetcode.com/problems/valid-number/',
         'sol_link': '',
         'name': 'Valid Number',
         'company': 'fb',
         'number': 65,
         'difficulty': 'Hard',
         'topics': 'String'},
        {'lc_link': 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock/',
         'sol_link': '',
         'name': 'Best Time to Buy and Sell Stock',
         'company': 'uber',
         'number': 121,
         'difficulty': 'Easy',
         'topics': 'Array, Dynamic Programming'},
        {'lc_link': 'https://leetcode.com/problems/valid-palindrome/',
         'sol_link': '',
         'name': 'Valid Palindrome',
         'company': 'spotify',
         'number': 125,
         'difficulty': 'Easy',
         'topics': 'Two Pointers, String'},
        {'lc_link': 'https://leetcode.com/problems/happy-number/',
         'sol_link': '',
         'name': 'Happy Number',
         'company': 'twitter',
         'number': 202,
         'difficulty': 'Easy',
         'topics': 'Hash Table, Math, Two Pointers'},
        {'lc_link': 'https://leetcode.com/problems/single-number-iii/',
         'sol_link': '',
         'name': 'Single Number III',
         'company': 'fb',
         'number': 260,
         'difficulty': 'Medium',
         'topics': 'Array, Bit Manipulation'},
        {'lc_link': 'https://leetcode.com/problems/find-median-from-data-stream/',
         'sol_link': '',
         'name': 'Find Median from Data Stream',
         'company': 'microsoft',
         'number': 295,
         'difficulty': 'Hard',
         'topics': 'Two Pointers, Design, Sorting, Heap, Data Stream'},
    ]
    
    return render_template('problems.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host = '127.0.0.1', debug = True)