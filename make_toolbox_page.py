#!/usr/bin/python3

"""This script creates a Markdown files with a list of m8f's toolbox
parts with the corresponding versions and links."""

from os import chdir
from os import path
from os import getcwd
from subprocess import PIPE
from subprocess import run

SRC_DIR = path.expanduser('~/src/')
TOPIC_URL = 'https://forum.zdoom.org/viewtopic.php?f=43&t='

"""Title, directory/repository, ZDF topic"""
TOOLBOX_PARTS = [
    ['10.5x'                , '10.5x'               , '65962', 'enemy multiplier/divider'],
    ['Armament Tuning'      , 'armament-tuning'     , '61079', 'extra options for weapon tweaking'],
    ['Autoautosave'         , 'autoautosave'        , '59889', 'universal automatic autosaver'],
    ['Death-flip'           , 'death-flip'          , '66117', 'mirrored death animations'],
    ['dps-widget'           , 'dps-widget'          , '70954', 'damage per second on-screen widget'],
    ['Floor Mod'            , 'floor-mod'           , '76193', 'makes damaging floors configurable'],
    ['Gearbox'              , 'gearbox'             , '71086', 'fancy weapon/item selection'],
    ['Graveyard'            , 'graveyard'           , '68835', 'places gravestones where you die'],
    ['Hellscape Navigator'  , 'hellscape-navigator' , '61643', 'tools to help navigation'],
    ['Laser Sight'          , 'laser-sight'         , '61079', 'standalone laser sight'],
    ['m_Gizmos'             , 'm_gizmos'            , '61079', 'weapon-related accessories'],
    ['Mod Menu'             , 'mod-menu'            , '76206', 'moves mod options to a submenu'],
    ['Nomina'               , 'nomina'              , '68528', 'custom names for weapons and monsters'],
    ['Precise Crosshair'    , 'precise-crosshair'   , '64788', 'places crosshair where you shoot'],
    ['Sound to Screen'      , 'sound-to-screen'     , '75335', 'shows sounds on screen'],
    ['Status Widget'        , 'status-widget'       , '72283', 'tracks health, armor, ammo, items'],
    ['Target Spy'           , 'target-spy'          , '60784', 'health bar for targeted enemies'],
    ['Ultimate Custom Doom' , 'ultimate-custom-doom', '64678', 'deep game customization'],
    ['Warm Reception'       , 'warm-reception'      , '69486', 'alters enemy behavior on level start'],
]
TOOLBOX_HEADER = """# m8f's toolbox

A collection of add-ons for [GZDoom](https://zdoom.org/index) game engine.

"""

TOOLBOX_FOOTER = """
See also my [other Doom stuff](https://mmaulwurff.github.io/pages/stuff) and [m8f's doctor's bag](https://mmaulwurff.github.io/pages/doctors-bag).
"""

DOCTORS_BAG_PARTS = [
    ['Mod Compatibility Checklist',
     'mod-compatibility-checklist',
     '71762',
     'for more robust mods and better bug reports'],

    ['Zabor',
     'zabor',
     '71569',
     'VM abort handler for better bug reports'],
]

DOCTORS_BAG_HEADER = """# m8f's doctor's bag

A collection of add-ons for [GZDoom](https://zdoom.org/index) game engine to help mod development.

"""

DOCTORS_BAG_FOOTER = """
See also my [other Doom stuff](https://mmaulwurff.github.io/pages/stuff) and [m8f's toolbox](https://mmaulwurff.github.io/pages/toolbox).
"""

def make_page(filename, header, parts, footer):
    """Creates a Markdown file with the list."""

    current_path = getcwd()

    out = open(filename, 'w')
    out.write(header)

    for part in parts:

        srcpath = ''.join([SRC_DIR, part[1]])
        chdir(srcpath)

        command = ['git', 'describe', '--abbrev=0', '--tags']
        version = run(command, stdout=PIPE).stdout.decode('utf-8').rstrip()
        url = ''.join([TOPIC_URL, part[2]])
        shield = ''.join(['<img src="https://img.shields.io/github/downloads/mmaulwurff/',
                          part[1],
                          '/total?color=white&label=%20&style=plastic" title="downloads">'])
        line = ''.join(['[', part[0], ' (', version, ')](', url, ') - ',
                        part[3], ' ', shield, '\n\n'])

        out.write(line)

    out.write(footer)
    chdir(current_path)


if __name__ == "__main__":

    make_page('toolbox.md', TOOLBOX_HEADER, TOOLBOX_PARTS, TOOLBOX_FOOTER)
    make_page('doctors-bag.md', DOCTORS_BAG_HEADER, DOCTORS_BAG_PARTS, DOCTORS_BAG_FOOTER)
