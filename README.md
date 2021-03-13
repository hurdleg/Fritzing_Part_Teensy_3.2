# Fritzing Part - Teensy 3.2
## Description
The Teensy is a complete USB-based microcontoller development system, in a very small footprint, capable of implementing many types of projects. All programming is done via the USB port. No special programmer is needed, only a standard micro-USB cable and a PC or Macintosh with a USB port. It has a USB keyboard/mouse/joystick emulation stack and can be programmed through Arduino IDE.

For more information: http://www.pjrc.com/teensy

## Breadboard
![Teensy 3.2. breadboard](./core/svg/breadboard/Teensy_3.2_breadboard.svg)

## Icon
![Teensy 3.2. icon](./core/svg/icon/Teensy_3.2_icon.svg)

## PCB
![Teensy 3.2. pcb](./core/svg/pcb/Teensy_3.2_pcb.svg)

## Schematic
![Teensy 3.2. schematic](./core/svg/schematic/Teensy_3.2_schematic.svg)

***

# Installation
1. Copy file `Teensy_3.2.fzpz` to folder `$FRITZING_HOME/bins`
2. Launch `fritzing` app and import `Teensy_3.2.fzpz` into Parts bin named: **My Parts**
![Import Teensy_3.2.fzpz](./unit-test/uat-Teensy_3.2_breadboard.png)

# Onboard LED
To turn on the onboard LED (digital pin 13), edit `./core/svg/breadboard/Teensy_3.2_breadboard.svg` and change the **fill** attribute to: #F37220

    <!-- TODO :: Onboard LED :: orange #F37220 -->
    <rect id="_x30_.16" x="88.887" y="8.368" fill="#333333" width="5.704" height="2.101"/>

### Enjoy!
### @author Gerald.Hurdle@AlgonquinCollege.com