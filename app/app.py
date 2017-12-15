#!/usr/bin/env python
#-*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for, redirect
import random

import mad_libs as ml

app = Flask(__name__)

final_story = ''

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Was 'Nice' or 'Naughty' clicked?
        if "nice" in request.form:
            status = 'nice'
        else:
            status = 'naughty'
        return redirect(url_for('mad_libs_form', status=status))

    else:
        global final_story
        final_story = ''
        return render_template("home.html")

@app.route('/mad_libs_form/<status>', methods=['GET', 'POST'])
def mad_libs_form(status):
    if request.method == 'POST':
        story = request.form['story']

        # If story is in mad_libs dict correctly, the story list should be 1 element longer than the fill_ins list
        story_list = break_story_into_list(story)
        if status == 'nice':
            fill_ins = ml.nice_mad_libs[story]
        else:
            fill_ins = ml.naughty_mad_libs[story]

        global final_story
        final_story = ''
        for i in range(0, len(fill_ins)):
            final_story += story_list[i]
            final_story += request.form[fill_ins[i]].upper()
        # Get the final element of story_list
        final_story += story_list[-1]
        # Unicode is being encoded to ASCII and I'm getting errors if I don't ignore the chars that can't be encoded in ASCII
        final_story = final_story.encode('ascii', 'ignore')
        return redirect(url_for('final'))
    else:
        if status == 'nice':
            (story, fill_ins) = choose_random_mad_lib(ml.nice_mad_libs)
        else:
            (story, fill_ins) = choose_random_mad_lib(ml.naughty_mad_libs)
        return render_template('mad_libs_form.html', status=status, form_list=fill_ins, story=story)

@app.route('/final', methods=['GET', 'POST'])
def final():
    if request.method == 'POST':
        if "start_over" in request.form:
            return render_template(url_for('index'))
    else:
        global final_story
        app.logger.debug("final story is {}".format(final_story))
        return render_template("final.html", story=final_story)


### Non-routing functions

def break_story_into_list(story):
    return story.split(ml.FILL_IN_PTRN)

def choose_random_mad_lib(mad_libs):
    return random.choice( list(mad_libs.iteritems()) )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
