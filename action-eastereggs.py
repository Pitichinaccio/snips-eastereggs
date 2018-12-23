#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io

CONFIGURATION_ENCODING_FORMAT = "utf-8"
# CONFIG_INI = "config.ini"

def subscribe_intent_callback(hermes, intentMessage):
    intentname = intentMessage.intent.intent_name
    if intentname == "bertron:Fuchs":
        result_sentence = "Whoa  papapapapapapapo"
        hermes.publish_end_session(intentMessage.session_id, result_sentence)

    elif intentname == "bertron:Crystal":
        result_sentence = "Herzlichen Glyckwunsch ich bin doch nicht schwanger Sie haben das setup abgeschlossen"
        hermes.publish_end_session(intentMessage.session_id, result_sentence)
        
     elif intentname == "bertron:Schoenste":
        result_sentence = "Frau Kynigin, Ihr seid die Schynste hier, aber Schneewittchen hinter den sieben Bergen, bei den sieben Zwergen ist noch tausend Mal schyner als Ihr"
        hermes.publish_end_session(intentMessage.session_id, result_sentence)       
        
if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intents(subscribe_intent_callback).start()

