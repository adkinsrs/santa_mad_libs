#!/usr/bin/env python
#-*- coding: utf-8 -*-
from flask import Flask, render_template, request
import random

import mad_libs as ml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        story = request.form['story']

        # If story is in mad_libs dict correctly, the story list should be 1 element longer than the fill_ins list
        story_list = break_story_into_list(story)
        fill_ins = ml.mad_libs[story]
        final_story = ''
        for i in range(0, len(fill_ins)):
            final_story += story_list[i]
            final_story += request.form[fill_ins[i]].upper()
        # Get the final element of story_list
        final_story += story_list[-1]
        # Unicode is being encoded to ASCII and I'm getting errors if I don't ignore the chars that can't be encoded in ASCII
        final_story = final_story.encode('ascii', 'ignore')
        return '<p style="font-size:150%;">{}</p>'.format(final_story)
    else:
        (story, fill_ins) = choose_random_mad_lib()
        return render_template('mad_libs_form.html', form_list=fill_ins, story=story)

### Non-routing functions

def break_story_into_list(story):
    return story.split(ml.FILL_IN_PTRN)

def choose_random_mad_lib():
    return random.choice( ml.mad_libs.keys() )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
