import json
from html import entities

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    with open('entities.json') as f:
        entities = json.load(f)
        return render_template("main-all-items.html", entities=entities)


@app.route('/paging')
def paging():
    return render_template("main.html")


@app.route('/search')
def search():
    model = request.args.get('model')
    with open('entities.json') as f:
        entities = json.load(f)
        response = []
        if not model:
            response = entities
        else:
            for e in entities:
                if e["model"] == model:
                    response.append(e)
        return render_template("search_ause.html", entities=response)


@app.route('/card/<int:eid>')
def card(eid: int):
    card_full = []
    for ent in entities:
        if ent["id"] == eid:
            card_full.append(ent)
    return render_template("card_full.html", entities=card_full)


@app.route('/short/<int:eid>')
def short(eid: int):
    short_card = []
    for ent in entities:
        if ent["id"] == eid:
            short_card.append(ent)
    return render_template("card_short.html", entities=short_card)


if __name__ == '__main__':
    app.run(debug=True)
