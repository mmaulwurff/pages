#!/usr/bin/python3

"""This script creates a Markdown files with a list of m8f's toolbox
parts with the corresponding versions and links."""

from os import chdir
from os import path
from subprocess import PIPE
from subprocess import run

SRC_DIR = path.expanduser('~/Documents/src/')
TOPIC_URL = 'https://forum.zdoom.org/viewtopic.php?f=43&t='

PARTS = [
    ['Target Spy: Health Bars++' , 'target-spy'          , '60784'],
    ['Autoautosave'              , 'autoautosave'        , '59889'],
    ['Hellscape Navigator'       , 'hellscape-navigator' , '61643'],
    ['Weapon Menu +'             , 'weapon-menu'         , '59498'],
    ['IDCLEVer Starter'          , 'idclever-starter'    , '61079'],
    ['Armament Tuning'           , 'armament-tuning'     , '61079'],
    ['Laser Sight'               , 'laser-sight'         , '61079'],
    ['Pomodoro Timer'            , 'gzdoom-pomodoro'     , '60035'],
]

if __name__ == "__main__":

    OUT = open('toolbox.md', 'w')

    OUT.write("# m8f's toolbox\n\n")

    for part in PARTS:

        path = ''.join([SRC_DIR, part[1]])
        chdir(path)

        command = ['git', 'describe', '--abbrev=0', '--tags']
        version = run(command, stdout=PIPE, stderr=PIPE).stdout.decode('utf-8').rstrip()

        url = ''.join([TOPIC_URL, part[2]])
        OUT.write(''.join(['- [', part[0], ' (v', version, ')' '](', url, ')\n']))
