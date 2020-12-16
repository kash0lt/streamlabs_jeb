import json
import os
import codecs

# this should work ouyt to be a jeb command in Streamlabs Chatbot
ScriptName = "Jeb"
Website = "https://github.com/kash0lt/streamlabs_jeb"
Description = "Jeb - the judge of kerbalness."
Creator = "Padre_San"
Version = "1.0.1"
Command = "!jeb"

settings = {}


def Init():
    global settings
    work_dir = os.path.dirname(__file__)
    with codecs.open(os.path.join(work_dir, "settings.json"), encoding='utf-8-sig') as json_file:
        settings = json.load(json_file, encoding='utf-8-sig')
    return


def Execute(data):
    if data.GetParam(0) != Command or Parent.IsOnUserCooldown(ScriptName, Command, data.User):
        return
    whodis = data.UserName
    send_message("Alright, the result for " + whodis + " is that you are " + str(Amount_Kerbalness()) + "% kerbal.")
    if whodis != Creator:
        Parent.AddUserCooldown(ScriptName, Command, whodis, settings["userCoolDown"])
    return


def Tick():
    return


def send_message(message):
    Parent.SendStreamMessage(message)
    return


def Amount_Kerbalness():
    percent_kerbal = Parent.GetRandom(0, 100)
    return percent_kerbal


def log(message):
    Parent.Log(Command, message)
    return
