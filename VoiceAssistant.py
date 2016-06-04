import sys
from MusicHandler import MusicHandler
import Speech

reload(sys)
sys.setdefaultencoding('Cp1252')  # fix for unicode file names in windows

voice_handlers = {"music": MusicHandler}

print("Say something!")
user_input = Speech.listen()
print("I heard you say \"{}\"".format(user_input))

for keyword, handler in voice_handlers.iteritems():
    if keyword in user_input:
        handler(user_input)
