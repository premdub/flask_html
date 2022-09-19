from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello world, WWW!'

@app.route('/')
def homepage():
    return render_template('p1.html')

@app.route('/styled_layout')
def homepage_styles_layout():
    return render_template('p2_homepage_withCSS_layout.html') 
    # import to note that it is going to look for the .html files in a folder called templates

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
