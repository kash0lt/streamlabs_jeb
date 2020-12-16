# this should work ouyt to be a jeb command in Streamlabs Chatbot
ScriptName = "Jeb"
Website = "https://github.com/kash0lt/streamlabs_jeb"
Description = "Jeb - the judge of kerbalness."
Creator = "Padre_san"
Version = "1.0.1"
Command = "!jeb"


def Init():
    return


def Execute(data):
    if data.GetParam(0) != Command:
        return
    whodis = data.UserName
    send_message("Alright, the result for " + whodis + " is that you are " + str(Amount_Kerbalness()) + "% kerbal.")
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
