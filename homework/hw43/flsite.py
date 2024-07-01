from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '5aa6f7ec22a1f5546b2eee1491098e132ae36001'

menu = [
    {'name': 'Main page', 'url': 'main'},
    {'name': 'About Us', 'url': 'about'},
    {'name': 'Catalog', 'url': 'catalog'},
    {'name': 'Contact Us', 'url': 'contact'}
]


@app.route('/')
@app.route('/main')
def index():
    return render_template('main.html', title="Advancing Enterprise AI", menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title="About Us", menu=menu)


@app.route('/catalog')
def catalog():
    return render_template('catalog.html', title="Catalog", menu=menu)


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 5 and len(request.form['message']) > 1:
            flash("Message delivered. Thank you", category="success")
        else:
            flash("Message undelivered!!!", category="fail")
    return render_template('contact.html', title="Contact Us", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Page not found :(", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
