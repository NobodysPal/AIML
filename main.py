#!/usr/bin/env python

import aiml
import os
import glob
import subprocess

scriptPath = os.getcwd()

# Builds the startup.xml
def buildStartup():
    basePath = os.path.join(scriptPath, "aiml", "*.aiml")
    aimls = glob.glob(basePath)

    f = open('startup.xml', 'w')
    f.write("<aiml version=\"1.0.1\" encoding=\"UTF-8\">\n"
            "\t<category>\n"
            "\t\t<pattern>LOAD AIML B</pattern>\n"
            "\t\t<template>\n")
    f.close()
    for aiml in aimls:
        f = open('startup.xml','a')
        f.write("\t\t\t<learn>" + aiml + "</learn>\n")
        f.close()
    f = open('startup.xml', 'a')
    f.write("\t\t</template>\n"
            "\t</category>\n"
            "</aiml>")
    f.close()

# The Bot voice on a windows system
def saySomething(phrase):
    basePath = os.path.join(scriptPath, "voice", "Say-Phrase.ps1")
    subprocess.Popen(["powershell", ". " + basePath + "; Say-Phrase -phrase \"" + phrase + "\""],
                     stdout=subprocess.PIPE)

# Starts the Bot
def aimlBot():
    # Create the kernel and learn AIML files
    kernel = aiml.Kernel()
    kernel.learn("startup.xml")
    kernel.respond("load aiml b")

    # Starts the bot loop
    while True:
        message = raw_input("Enter your message to the bot: ")
        if message == "quit":
            exit()
        elif message == "save":
            kernel.saveBrain("brain.brn")
        else:
            bot_response = kernel.respond(message)
            print bot_response
            saySomething(bot_response)
            # Do something with bot_response

# Main functions
if __name__ == "__main__":
    buildStartup()
    aimlBot()
