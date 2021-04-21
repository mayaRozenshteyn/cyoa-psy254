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
    "q0": {"title": "Congratulations on becoming a parent! A few weeks after taking your newborn home from the hospital, you notice that they spend over 5 hours each day crying. Frustrated, you do a quick Google search and discover that the average baby spends only about 2 hours per day crying. How do you proceed?", "c1": "Shake your baby until they stop crying", "c1id": "q1", "c2": "Take them to the hospital", "c2id": "q2"},
    "q1": {"title": "Be careful!! Shaking your child is very dangerous and might result in Shaken Baby Syndrome, a potentially life-threatening condition. Luckily, your child ends up okay. Now you must decide whether to breastfeed or bottlefeed. Which do you choose?", "c1": "Breastfeed", "c1id": "q3", "c2": "Bottlefeed", "c2id": "q4"},
    "q2": {"title": "It was very astute of you to take your child to the hospital, as it turns out they have colic! Luckily, the pacifier and white noise machine your baby’s doctor recommended help ease the crying. Now you have a greater opportunity to bond with your child. How do you prefer to interact with them?", "c1": "Reading aloud to them", "c1id": "q5", "c2": "Playing fun games like Peekaboo", "c2id": "q6"},
    "q3": {"title": "Great! Breastfeeding helps promote your child’s immune system and facilitates brain development. You would like to do even more to facilitate their brain development. What toy do you pick to help you with this?", "c1": "Electronic activity cube", "c1id": "q7", "c2": "Cardboard box", "c2id": "q8"},
    "q4": {"title": "Uh oh, your child was lacking some of the cognitive benefits of breastfeeding and you notice them lagging slightly behind neurotypical children of their same age. You would like to do something to facilitate their brain development. What toy do you pick to help you with this?", "c1": "Electronic activity cube", "c1id": "q7", "c2": "Cardboard box", "c2id": "q8"},
    "q5": {"title": "High quality language input is a great way to help your child start to comprehend and produce language! Your child is a little older now and you want them to continue along their trajectory of language growth (and general cognitive growth as well). How do you generally have them spend their time?", "c1": "Doing flashcards", "c1id": "q9", "c2": "At playdates", "c2id": "q10"},
    "q6": {"title": "The high-pitch speech characteristic of Peekaboo is a great way to help your child start to comprehend and produce language! And it makes them giggle :). Your child is a little older now and you want them to continue along their trajectory of language growth (and general cognitive growth as well). How do you generally have them spend their time?", "c1": "Doing flashcards", "c1id": "q9", "c2": "At playdates", "c2id": "q10"},
    "q7": {"title": "Unfortunately, though your child is quite focused when playing the the electronic cube, they are often quietly playing with the cube rather than listening to you speak, and their language development seems to be slower than other children you observe. Your child is a little older now and you want to remedy these language issues. How do you generally have them spend their time?", "c1": "Doing flashcards", "c1id": "q9", "c2": "At playdates", "c2id": "q10"},
    "q8": {"title": "Congratulations, you’ve just won the award for number one parent! Your child loves the cardboard box so much that they play with it on a daily basis, transforming it into fictional landscapes such as princess castles and a pirate ships. This makes them quite happy, which makes you quite happy as well. Your positive relationship with your child as well as the cognitive benefits they receive from imaginative play propel them (though not without ups and down, of course) to excel in the rest of their life. They become so interested in the effects of children’s toys on development that they eventually become a researcher at the Princeton Baby Lab :))!", "c1": "The End", "c1id": "s", "c2": "Restart", "c2id": "s"},
    "q9": {"title": "Your child starts to resent you for stifling their play and constantly forcing them to sit still and “study.” When you come back to your child after leaving a room, they tend to avoid eye contact with you :(. How do you attempt to remedy this? ", "c1": "You watch back home videos to better understand their feelings", "c1id": "q11", "c2": "You start to cuddle with them on the couch every evening", "c2id": "q11"},
    "q10": {"title": "Great choice! The cognitive demands of imaginative play are often greater than those required to study flashcards, and your child is well on their way to academic success. When they do start school, they get a perfect score on their very first test! What do you say to them?", "c1": "Awesome, your hard work paid off!", "c1id": "q12", "c2": "Wow, you’re so smart!", "c2id": "q13"},
    "q11": {"title": "This is a great way to bond with your child and improve your relationship with them! Your child can tell that you love them very much, so they start to ask you for toys very frequently and they get frustrated when you don’t allow them to get a certain toy. What do you do to help mitigate this behavior?", "c1": "Always consider their wishes, but say no when appropriate", "c1id": "q14", "c2": "Let them have whatever toys they want since they’re only a child once", "c2id": "q15"},
    "q12": {"title": "Praising your child’s process motivates them to keep working hard. In fact, they become so invested in their own learning and children’s perception of their own learning abilities that they go on to study educational psychology in college. Congratulations on being a great parent :)!!", "c1": "The End", "c1id": "s", "c2": "Restart", "c2id": "s"},
    "q13": {"title": "Praising your child’s intelligence causes them to feel pressure to perform and meet your standards. This frequent, self-inflicted pressure causes them to develop an anxiety-related disorder later in life. You don’t realize that your praise is the source of your child’s stress, but you do notice that your child seems less stressed when listening to music. When you see them feeling a little down one day, whose music do you play them?", "c1": "Taylor Swift", "c1id": "q16", "c2": "Harry Styles", "c2id": "q16"},
    "q14": {"title": "This authoritative parenting style proves to be very successful and your child seems to have high cognitive and social competence as a result. You decide it’s time to get them involved in some extracurriculars. What do you choose?", "c1": "Piano & Violin", "c1id": "q17", "c2": "You let them explore their interests", "c2id": "q18"},
    "q15": {"title": "Though this permissive behavior does foster warm feelings between you and your child, they continue to exhibit poor impulse control and anger management later in life, eventually turning to alcohol as a coping mechanism. However, you do send them to a rehabilitation facility where they meet with an excellent therapist. This therapist helps them improve their impulse control and addictive tendencies (though they do have a couple of relapses), and they go on to live a nice, simple life as an interior designer and a cat-lover.", "c1": "The End", "c1id": "s", "c2": "Restart", "c2id": "s"},
    "q16": {"title": "Great choice! Your child loves their music so much that they decide to start learning guitar. They experience exponential growth and, after high school, they start a band with some of their friends. The band becomes hugely successful, but the stress of great fame compounded with their anxiety-related disorder eventually causes them to quit the band. They move to a goat farm in Siberia, where they happily play guitar every Sunday for the other village people.", "c1": "The End", "c1id": "s", "c2": "Restart", "c2id": "s"},
    "q17": {"title": "Amy Chua? Is that you? Why are you playing this game? Your children are grown adults already. They’re probably fine, though they probably also resent you a little for restricting their childhoods. But I guess you’ve sold a lot of books so you still win the game...yay?", "c1": "The End", "c1id": "s", "c2": "Restart", "c2id": "s"},
    "q18": {"title": "Excellent! Your child realizes that they love swimming and joins a local swim team! They love to swim so much that they become a swim coach at the YMCA in their hometown, where they do their best to run an inclusive swim team and impart the same values of kindness and determination that you imparted on them onto their swimmers.", "c1": "The End", "c1id": "s", "c2": "Restart", "c2id": "s"}
}

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
def index():  
    return make_response(render_template('index.html'))

@app.route('/question', methods=['GET'])
def question():
    if request.args.get('q') == 's':
        return make_response(render_template('index.html'))
    question = q_dict[request.args.get('q')]["title"]
    c1 = q_dict[request.args.get('q')]["c1"]
    c2 = q_dict[request.args.get('q')]["c2"]
    c1id = q_dict[request.args.get('q')]["c1id"]
    c2id = q_dict[request.args.get('q')]["c2id"]
    return make_response(render_template('question.html', question=question, c1=c1, c2=c2, c1id=c1id, c2id=c2id))