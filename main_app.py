

from flask import Flask, redirect, url_for, render_template, request, session, g
from flask_sqlalchemy import SQLAlchemy


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


users = []
users.append(User(id=1, username='Anthony', password='password'))
users.append(User(id=2, username='Becca', password='secret'))
users.append(User(id=3, username='Carlos', password='somethingsimple'))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///primeira_liga.sqlite'
db = SQLAlchemy(app)

class ppl2021(db.Model):
   id = db.Column('Team Position', db.Integer, primary_key = True)
   Name = db.Column(db.String(100))
   Points = db.Column(db.Integer)
   Games_Played = db.Column(db.Integer)
   Win = db.Column(db.Integer)
   Draw = db.Column(db.Integer)
   Lose = db.Column(db.Integer)
   Goals_Scored = db.Column(db.Integer)
   Goals_Concerned = db.Column(db.Integer)



# db.create_all()


import requests
import json
import sqlite3


# url = "https://api-football-v1.p.rapidapi.com/v3/standings"

# querystring = {"season":"2021", "league":"94"}

# headers = {
# 	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
# 	"X-RapidAPI-Key": "68cd65fa40mshd0152fc63f9e5fep151d51jsn9ca3f6ffeb04"}

# response = requests.request("GET", url, headers=headers, params=querystring)


# result_json = response.text
# res = json.loads(result_json)
# res_structured = json.dumps(res, indent=4)
# # print(res_structured)
# res = response.json()
#2
# with open('standings.json', 'w') as file:
# 	json.dump(res, file, indent=4)
#
#
#
# with open('standings.json') as file:
# 	res_dictionary = json.load(file)
#
# laliga = res_dictionary['response'][0]['league']['standings'][0]


# ცხრილში მოცემული იქნება ლალიგის 2021 წლის ცხრილი გუნდის დასახელება, ჩატარებული მატჩები, მოგება წაგება და ა.შ გუნდები დალაგებული იქნება პოზიციის მიხედვით ცხრილში 2021 წელს
# list_team_names = []
# list_team_points = []
# list_team_played = []
# list_team_win = []
# list_team_draw = []
# list_team_lose = []
# list_team_goals_scored = []
# list_team_goals_concerned = []
#
#
#
# for each in laliga:
# 	list_team_names.append(each['team']['name'])
# 	list_team_points.append(each['points'])
# 	list_team_played.append(each['all']['played'])
# 	list_team_win.append(each['all']['win'])
# 	list_team_draw.append(each['all']['draw'])
# 	list_team_lose.append(each['all']['lose'])
# 	list_team_goals_scored.append(each['all']['goals']['for'])
# 	list_team_goals_concerned.append(each['all']['goals']['against'])





# for i in range(len(list_team_names)):
#     db.session.add(ppl2021(Name=list_team_names[i], Points=list_team_points[i],Games_Played=list_team_played[i],
#                              Win=list_team_win[i], Draw=list_team_draw[i], Lose=list_team_lose[i], Goals_Scored=list_team_goals_scored[i], Goals_Concerned=list_team_goals_concerned[i]))
#     db.session.commit()




@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user


@app.route('/', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     session.pop('user_id', None)
    #
    #     username = request.form['username']
    #     password = request.form['password']
    #
    #     user = [x for x in users if x.username == username][0]
    #     if user and user.password == password:
    #         session['user_id'] = user.id
    #         return redirect(url_for('profile'))
    #
    #     return redirect(url_for('login'))
    #
    #
    # return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('profile'))
    return render_template('login.html')


@app.route('/profile')
def profile():




    # if not g.user:
    #     return redirect(url_for('login'))

    return render_template('profile.html')

@app.route('/index')
def index():
    if request.method == 'GET':
        info = ppl2021.query.all()
        print(info)
        print('2')
        return render_template('index.html', info=info)

    # return render_template('index.html')






