from flask import Flask, render_template, request, flash, g
import sqlite3
import os
from FDataBase import FDataBase


DEBUG = True
SECRET_KEY = '4c85b99345380ce732bbb195a45cb0cf2e74c00f'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'hw.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('hw_db.sql', "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
        return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu(), title="Pricing", curses=dbase.get_curse_announce())


@app.route("/add_curse", methods=["POST", "GET"])
def add_curse():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["cost"]) > 4 and len(request.form["curse"]) > 4:
            res = dbase.add_curse(request.form["name"], request.form["cost"], request.form["curse"])
            if not res:
                flash("Ошибка добавления курса", category='error')
            else:
                flash("Курс добавлен успешно", category='success')
        else:
            flash("Ошибка добавления курса", category='error')

    return render_template('add_curse.html', menu=dbase.get_menu(), title="Добавление курса")


@app.route("/curse/<int:id_curse>")
def show_curse(id_curse):
    db = get_db()
    dbase = FDataBase(db)

    title, cost, text = dbase.get_curse(id_curse)
    return render_template('curse.html', menu=dbase.get_menu(), title=title, cost=cost, text=text)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())


if __name__ == '__main__':
    app.run()
