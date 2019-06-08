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
    ['Target Spy: Health Bars++' , 'target-spy'          , '60784#p1057216'],
    ['Autoautosave'              , 'autoautosave'        , '59889#p1045558'],
    ['Hellscape Navigator'       , 'hellscape-navigator' , '61643#p1068272'],
    ['Weapon Menu +'             , 'weapon-menu'         , '59498#p1040474'],
    ['IDCLEVer Starter'          , 'idclever-starter'    , '61079#p1060800'],
    ['Armament Tuning'           , 'armament-tuning'     , '61079#p1060800'],
    ['Laser Sight'               , 'laser-sight'         , '61079#p1060800'],
    ['Pomodoro Timer'            , 'gzdoom-pomodoro'     , '60035#p1047347'],
    ['Ultimate Custom Doom'      , 'ultimate-custom-doom', '64678#p1103556'],
    ['Precise Crosshair'         , 'precise-crosshair'   , '64788#p1104858'],
]
HEADER = """# m8f's toolbox

A collection of minimods for [GZDoom](https://zdoom.org/index) game engine.

[itch.io page](https://m8f.itch.io/m8fs-toolbox)

"""


if __name__ == "__main__":

    OUT = open('toolbox.md', 'w')
    OUT.write(HEADER)

    for part in PARTS:

        path = ''.join([SRC_DIR, part[1]])
        chdir(path)

        command = ['git', 'describe', '--abbrev=0', '--tags']
        version = run(command, stdout=PIPE).stdout.decode('utf-8').rstrip()

        url = ''.join([TOPIC_URL, part[2]])
        OUT.write(''.join(['- [', part[0], ' (v', version, ')](', url, ')\n']))
