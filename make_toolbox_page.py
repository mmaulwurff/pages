#!/usr/bin/python3

"""This script creates a Markdown files with a list of m8f's toolbox
parts with the corresponding versions and links."""

from os import chdir
from os import path
from subprocess import PIPE
from subprocess import run

SRC_DIR = path.expanduser('~/src/')
TOPIC_URL = 'https://forum.zdoom.org/viewtopic.php?f=43&t='

"""Title, directory/repository, ZDF topic"""
PARTS = [
    ['10.5x'                     , '10.5x'               , '65962'],
    ['Armament Tuning'           , 'armament-tuning'     , '61079'],
    ['Autoautosave'              , 'autoautosave'        , '59889'],
    ['Autopause'                 , 'autopause'           , '67991'],
    ['Death-flip'                , 'death-flip'          , '66117'],
    ['dps-widget'                , 'dps-widget'          , '70954'],
    ['Gearbox'                   , 'gearbox'             , '71086'],
    ['Graveyard'                 , 'graveyard'           , '68835'],
    ['Hellscape Navigator'       , 'hellscape-navigator' , '61643'],
    ['IDCLEVer Starter'          , 'idclever-starter'    , '61079'],
    ['Laser Sight'               , 'laser-sight'         , '61079'],
    ['m_Gizmos'                  , 'm_gizmos'            , '61079'],
    ['Nomina'                    , 'nomina'              , '68528'],
    ['Pomodoro Timer'            , 'gzdoom-pomodoro'     , '60035'],
    ['Precise Crosshair'         , 'precise-crosshair'   , '64788'],
    ['Target Spy: Health Bars++' , 'target-spy'          , '60784'],
    ['Ultimate Custom Doom'      , 'ultimate-custom-doom', '64678'],
    ['Warm Reception'            , 'warm-reception'      , '69486'],
]
HEADER = """# m8f's toolbox

A collection of minimods for [GZDoom](https://zdoom.org/index) game engine.

<a href="https://forum.zdoom.org/viewtopic.php?f=4&t=60112#p1048497">
<img src="https://mmaulwurff.github.io/zdoom-top-labels/pngs/m8f%E2%80%99s_toolbox.png">
</a>

"""

FOOTER = """
See also my [other Doom stuff](https://mmaulwurff.github.io/pages/stuff).
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
        shield = ''.join(['<img src="https://img.shields.io/github/downloads/mmaulwurff/', part[1], '/total?color=white&label=%20&style=plastic" title="downloads">'])
        line = ''.join(['[', part[0], ' (', version, ')](', url, ') ', shield, '\n\n'])

        OUT.write(line)

    OUT.write(FOOTER)
