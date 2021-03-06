import json
from html import entities

from flask import Flask, render_template, request

app = Flask(__name__)


with open('entities.json', encoding='utf-8') as f:
    entities = json.load(f)


@app.route('/')
def index():
    return render_template("main-all-items.html", entities=entities)


@app.route('/paging')
def paging():
    return render_template("main.html")


@app.route('/search/')
def search():
    model = str(request.args.get('model'))
    model = model.split(' ')
    response = []
    if not model:
        response = entities
    else:
        for i in model:
            for e in entities:
                for ent in e["model"].split(' '):
                    if ent == i:
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
