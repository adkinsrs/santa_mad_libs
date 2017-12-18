# -*- coding: utf-8 -*-

# Will house the list of Mad Libs that will be picked from random

# NOTE: Occasionally an odd byte character (0xe2) pops up in the story.  I found decoding the key in utf-8 resolves this

FILL_IN_PTRN = '___'

nice_mad_libs = {
    "Dear Santa,<br><br>I have been a very good ___ this year. I have contributed to ___ grant(s), have run at least ___ ___ analyses and have published in some really ___ journals. I never complain about the ___ my boss makes me deal with, and am always ___ to others in the ___. Therefore, I would like to ask for a ___ ___ this year. I've been wanting this for ___ years, and promise to ___ with it all year long! I'll be sure to leave ___ for you and ___ for the reindeer. Stay ___!<br><br>Your friend,<br>___".decode('utf-8') :
    ["JOB_TITLE","NUMBER", "ANOTHER NUMBER", "ADJECTIVE", "ANOTHER ADJECTIVE", "PLURAL NOUN", "ADJECTIVE, PLEASE!", "TYPE OF ROOM", "YET ANOTHER ADJECTIVE", "NOUN", "YET ANOTHER NUMBER", "VERB", "FOOD", "MORE FOOD", "LAST ADJECTIVE", "YOUR NAME"] ,

    "Dear Santa,<br><br>Well, it's that time again, the ___-est time of the year! I've been very ___ this year, and am hoping to find some ___ under my Christmas ___. Some of my friends are asking for ___ ___ this year, but there's only one thing that I really want... a(n) ___ ___! I hope that you can fit one in your sleigh! Please don't forget to ___ when you get to my house. I'll have plenty of ___ for you and will leave enough ___ for ___ reindeer!<br><br>Sincerely,<br>Your favorite ___, ___".decode('utf-8') :
    ["ADJECTIVE", "ANOTHER ADJECTIVE", "PLURAL NOUN", "NOUN", "ADJECTIVE, PLEASE", "ANOTHER PLURAL NOUN", "YET ANOTHER ADJECTIVE", "ANOTHER NOUN", "VERB", "FOOD", "MORE FOOD", "NUMBER", "JOB TITLE", "YOUR NAME"]

}

naughty_mad_libs = {
    "Dear ___ Santa,<br><br>Another ___ holiday season is here, and I'm going to get right to the point. I want ___! I also want a ___, a ___ and a ___! I've been really ___ this year, but I deserve these things for the ___ that I've had to put up with at work from my fellow ___s! Sure, I may have broken a few ___, and never ___ my work. And then of course there was the time I ___ that ___ to the boss. But can you forget all of that if I slip ___ bucks alongside the ___ under the tree on Christmas Eve? Don't consider it a bribe, consider it a ___.<br><br>Thanks,<br>___".decode('utf-8') :
    ["ADJECTIVE", "ANOTHER ADJECTIVE", "PLURAL NOUN", "NOUN", "ANOTHER NOUN", "YET ANOTHER NOUN", "ADJECTIVE, PLEASE", "ANOTHER PLURAL NOUN", "JOB TITLE", "YET ANOTHER PLURAL NOUN", "PAST TENSE VERB", "ANOTHER PAST TENSE VERB", "ONE MORE NOUN", "NUMBER", "FOOD", "LAST NOUN", "YOUR NAME"] ,

    "Dear Santa,<br><br>Well, it's that time again, the ___-est time of the year! Ive may not have been very nice this year, but I'm still hoping to find some ___ under my Christmas ___. A bunch of my friends are expecting coal or ___ this year, but I'm hoping that you'll take pity on me because I'm so ___ and bring me the one thing that I really want... a(n) ___ ___! I hope that you can fit one in your sleigh! Please don't forget to ___ when you get to my house. Enjoy the ___ and ___ for the reindeer!<br><br>Sincerely,<br>A very repentant ___, ___".decode('utf-8') :
    ["ADJECTIVE", "PLURAL NOUN", "NOUN", "ANOTHER PLURAL NOUN", "ANOTHER ADJECTIVE", "YET ANOTHER ADJECTIVE", "ANOTHER NOUN", "VERB", "FOOD", "MORE FOOD", "JOB TITLE", "YOUR NAME"]


}
