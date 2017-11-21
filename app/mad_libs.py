# -*- coding: utf-8 -*-

# Will house the list of Mad Libs that will be picked from random

# NOTE: Occasionally an odd byte character (0xe2) pops up in the story.  I found decoding the key in utf-8 resolves this

FILL_IN_PTRN = '___'

mad_libs = {
        "Dear Santa Claus,<br><br>My name is ___. How have you been this year? I know you must be very busy during this holiday season. Please say ___ to your elves and Mrs. Claus. I hope your reindeer are ready to ___ around the world. Please tell them there will be fresh ___ waiting for them and of course there will be ___ and ___ for you at my house. However, this year please try to be quiet when you deliver my presents because it is very important that I get a full ___ of sleep. I have been very ___ this year and did not cause any permanent damage to my ___... yet. I only want ___ things for Christmas so this should be an easy year for you. My first wish is for a ___ that will protect me from Christmas burglars and take me to school because let’s face it, gas is too expensive. I also love ___. These are the best inventions in the world and I want ___ of them. I would also like ___ to show up at my door on Christmas morning and serenade me with ___. Finally, I think that you should bring ___ to the world. I understand these things are hard to come by, but I have faith in you and your ___. If all of these things are too hard to get please make things easier on you and simply send ___. The only thing I don’t want for Christmas is a ___. I am putting my ___ in you Santa. Thanks for helping make this the best holiday ever.<br><br>Hugs and ___,<br><br>___".decode('utf-8') :
        ["YOUR NAME", "SALUTATION", "VERB", "NOUN", "FOOD", "BEVERAGE", "NUMBER + UNIT OF TIME", "ADJECTIVE", "TYPE OF FAMILY MEMBER", "NUMBER", "ANIMAL", "PLURAL NOUN", "NUMBER", "IGS EMPLOYEE", "SONG", "PLURAL NOUN", "PLURAL NOUN", "PLURAL NOUN", "NOUN", "NOUN", "PLURAL NOUN", "YOUR NAME"],
        "Dear Santa,<br><br>My name is ___, and all year I have been a very, very good ___. I have been ___ at school, and when my teacher asked me to VERB the blackboard, I just said, '___!' I have not ___ or ___. Not even once. And I have helped a lot of old ___ cross the street. Because I have been so ___, I am sure you are going to bing me a new ___ with ___ wheels. I would also like to have a ___ racquet. And a secret microphone so I can spy on ___ and learn all of his ___ secrets. Well, Santa, I know you will put all of these ___ presents in my ___ on Christmas. Or else I will have been good for nothing.".decode('utf-8') :
        ["YOUR NAME", "NOUN", "ADJECTIVE", "SILLY NOISE", "VERB - PAST TENSE", "VERB - PAST TENSE", "PLURAL NOUN", "ADJECTIVE", "NOUN", "ADJECTIVE", "TYPE OF SPORT", "IGS EMPLOYEE", "ADJECTIVE", "ADJECTIVE", "NOUN"]
    }
