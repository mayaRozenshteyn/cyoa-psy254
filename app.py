#!/usr/bin/env python

#-----------------------------------------------------------------------

# app.py
# Author: Maya Rozenshteyn

#-----------------------------------------------------------------------

from flask import Flask, request, make_response, redirect, url_for
from flask import render_template

#-----------------------------------------------------------------------

app = Flask(__name__,  template_folder='templates')

# "q": {"title": "", "c1": "", "c1id": "q", "c2": "", "c2id": "q"}

q_dict = {
    "q0": {"title": "Congratulations on becoming a parent! A few weeks after taking your newborn home from the hospital, you notice that they spend over 5 hours each day. Frustrated, you do a quick Google search and discover that the average baby spends only about 2 hours per day crying. How do you proceed?", "c1": "Shake your baby until they stop crying", "c1id": "q1", "c2": "Take them to the hospital", "c2id": "q2"},
    "q1": {"title": "Be careful!! Shaking your child is very dangerous and might result in Shaken Baby Syndrome, a potentially life-threatening condition. Luckily, your child ends up okay. Now you must decide whether to breastfeed or bottlefeed. Which do you choose?", "c1": "Breastfeed", "c1id": "q3", "c2": "Bottlefeed", "c2id": "q4"}
}

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
def index():  
    return make_response(render_template('index.html'))

@app.route('/question', methods=['GET'])
def question():
    question = q_dict[request.args.get('q')]["title"]
    c1 = q_dict[request.args.get('q')]["c1"]
    c2 = q_dict[request.args.get('q')]["c2"]
    c1id = q_dict[request.args.get('q')]["c1id"]
    c2id = q_dict[request.args.get('q')]["c2id"]
    return make_response(render_template('question.html', question=question, c1=c1, c2=c2, c1id=c1id, c2id=c2id))