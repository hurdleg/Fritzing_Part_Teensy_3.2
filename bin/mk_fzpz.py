#!/usr/bin/python
import os
import subprocess
from shutil import copyfile

PART = "Teensy_3.2"
PART_FILE = str(PART + ".fzp")
PART_BIN = str(PART + ".fzpz")
PART_ZIP = str("./part." + PART_FILE)
BREADBOARD = str(PART + "_breadboard.svg")
BREADBOARD_ZIP = str("./svg.breadboard." + BREADBOARD)
ICON = str(PART + "_icon.svg")
ICON_ZIP = str("./svg.icon." + ICON)
PCB = str(PART + "_pcb.svg")
PCB_ZIP = str("./svg.pcb." + PCB)
SCHEMATIC = str(PART + "_schematic.svg")
SCHEMATIC_ZIP = str("./svg.schematic." + SCHEMATIC)
ZIP_CMD = ["zip", PART_BIN, PART_ZIP, BREADBOARD_ZIP, ICON_ZIP, PCB_ZIP, SCHEMATIC_ZIP]

# Part
copyfile(str("./core/part/" + PART_FILE), PART_ZIP)

# Breadboard
copyfile(str("./core/svg/breadboard/" + BREADBOARD), BREADBOARD_ZIP)

# ICON
copyfile(str("./core/svg/icon/" + ICON), ICON_ZIP)

# PCB
copyfile(str("./core/svg/pcb/" + PCB), PCB_ZIP)

# SCHEMATIC
copyfile(str("./core/svg/schematic/" + SCHEMATIC), SCHEMATIC_ZIP)

# make the Fritzing .FZPZ file
subprocess.call(ZIP_CMD)

# clean-up unwanted files
os.remove(PART_ZIP)
os.remove(BREADBOARD_ZIP)
os.remove(ICON_ZIP)
os.remove(PCB_ZIP)
os.remove(SCHEMATIC_ZIP)
