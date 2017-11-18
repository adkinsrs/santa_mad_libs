#!/usr/bin/env python
from flask import Flask, render_template, request
import random

import mad_libs as ml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "You posted!"
    else:
        (story, fill_ins) = choose_random_mad_lib()
        story_list = break_story_into_list(story)
        # If story is in mad_libs dict correctly, the story list should be 1 element longer than the fill_ins list
        return render_template('mad_libs_form.html', form_list=fill_ins)

### Non-routing functions

def break_story_into_list(story):
    return story.split(ml.FILL_IN_PTRN)

def choose_random_mad_lib():
    return random.choice( list(ml.mad_libs.iteritems()) )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
