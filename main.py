from flask import Flask, render_template
from flask import json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', the_title='Home')

@app.route('/half_life_2_episode_two')
def half_life_2_episode_two():
    return render_template('half-life 2 episode two.html', the_title='Half-Life 2 Episode Two')

@app.route('/half_life')
def half_life():
    return render_template('half-life.html', the_title='Half-Life')

@app.route('/half_life_2')
def half_life_2():
    return render_template('half-life 2.html', the_title='Half-Life 2')
    
@app.route('/half_life_2_episode_one')
def half_life_2_episode_one():
    return render_template('half-life 2 episode one.html', the_title='Half-Life 2 Episode One')

@app.route('/portal')
def portal():
    return render_template('portal.html', the_title='Portal')

@app.route('/portal_2')
def portal_2():
    return render_template('portal 2.html', the_title='Portal 2')
    
@app.route('/portal_stories_mel')
def portal_stories_mel():
    return render_template('portal stories mel.html', the_title='Portal Stories Mel')

@app.route('/world_of_tanks')
def world_of_tanks():
    return render_template('world of tanks.html', the_title='World of Tanks')


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return render_template('error.html', code_=e.code, description_=e.description)
    
app.run()
