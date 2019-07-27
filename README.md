# Starling2Ledger

This is a GUI program written in Python that converts Starling Bank csv files into Ledger format.

# OSX Application

In order to make this script executable as any other application under OSX create an AppleScript:
```
do shell script "export LC_ALL=en_US.UTF-8; export LANG=en_US.UTF-8; /usr/local/bin/python3 '/Users/<USER>/<PATHTOSCRIPTFOLDER>/starling2ledger.py' &> /dev/null &"
```
and save it as an application.

