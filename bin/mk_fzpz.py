#!/usr/bin/python
import os
import subprocess
from shutil import copyfile

PART = "Teensy_3.2"
PART_FILE = str(PART + ".fzp")
PART_BIN = str(PART + ".fzpz")
PART_TAR = str("./part." + PART_FILE)
BREADBOARD = str(PART + "_breadboard.svg")
BREADBOARD_TAR = str("./svg.breadboard." + BREADBOARD)
ICON = str(PART + "_icon.svg")
ICON_TAR = str("./svg.icon." + ICON)
PCB = str(PART + "_pcb.svg")
PCB_TAR = str("./svg.pcb." + PCB)
SCHEMATIC = str(PART + "_schematic.svg")
SCHEMATIC_TAR = str("./svg.schematic." + SCHEMATIC)
TAR_CMD = ["tar", "-czf", PART_BIN, PART_TAR, BREADBOARD_TAR, ICON_TAR, PCB_TAR, SCHEMATIC_TAR]

# Part
copyfile(str("./core/part/" + PART_FILE), PART_TAR)

# Breadboard
copyfile(str("./core/svg/breadboard/" + BREADBOARD), BREADBOARD_TAR)

# ICON
copyfile(str("./core/svg/icon/" + ICON), ICON_TAR)

# PCB
copyfile(str("./core/svg/pcb/" + PCB), PCB_TAR)

# SCHEMATIC
copyfile(str("./core/svg/schematic/" + SCHEMATIC), SCHEMATIC_TAR)

# make the Fritzing .FZPZ file
subprocess.call(TAR_CMD)

# clean-up unwanted files
os.remove(PART_TAR)
os.remove(BREADBOARD_TAR)
os.remove(ICON_TAR)
os.remove(PCB_TAR)
os.remove(SCHEMATIC_TAR)
