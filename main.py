from flask import Flask
from utils import get_all, get_by_skill, get_by_pk

get_all()
app = Flask(__name__)


@app.route("/")
def page_index():
    return get_all()


@app.route("/candidates/<int:pk>")
def page_candidate(pk):
    return get_by_pk(pk)


@app.route("/skills/<skill>")
def page_skill(skill):
    skill_lower = skill.lower()
    return get_by_skill(skill_lower)


app.run()
