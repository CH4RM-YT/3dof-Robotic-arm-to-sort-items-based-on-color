# 3dof-Robotic-arm-to-sort-items-based-on-color

# Components

Arduino Uno R3

2x MG996r servo motors

1 Sg90 micro servo motors (2 sg90 servos can be used as well)

1 mg90s micro servo motor

A Bread Board

Male to female, male to male, and female to female jumper wires

Buck converter that can output 5v i used the lm2596 buck converter

Battery or power supply capabale of supplying at least 5A of current

# How to Connect the components

1. Connect the positive and negative terminals of your battery/power supply to the in+ and in- ends of the buck converter
2. If using and adjustable buck converter like the lm2596, adjust use a multi meter to check the outout voltage from the out+ and out- of       the buck converter and adjust the voltage to 5v
3. Connect a wire from the out+ and out- to the positive(+) and negative(-) bus strips on the breadboard
4. Connect one of the arduino's GND pins to the negative(-) bus strip of the bread board
5. Connect the brown/ground wire of the servos to the negative(-) bus strip of the bread board
6. Connect the red wire of the servo's to pins

