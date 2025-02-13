# 3dof-Robotic-arm-to-sort-items-based-on-color

# TABLE OF CONTENTS

-[Components](#Components)

-[Setup](#Setup)

-[Configuration](#Configuration)

-[Usage](#Usage)

# Components

Arduino Uno R3

2x MG996r servo motors (servos 1 and 2)

1 Sg90 micro servo motors (2 sg90 servos can be used as well) (servo3)

1 mg90s micro servo motor(servo 4)

A Bread Board

Male to female, male to male, and female to female jumper wires

Buck converter that can output 5v i used the lm2596 buck converter

Battery or power supply capabale of supplying at least 5A of current

A 3d printer to print the arm structure

# Setup

1. Connect the positive and negative terminals of your battery/power supply to the in+ and in- ends of the buck converter
2. If using and adjustable buck converter like the lm2596, adjust use a multi meter to check the outout voltage from the out+ and out- of       the buck converter and adjust the voltage to 5v
3. Connect a wire from the out+ and out- to the positive(+) and negative(-) bus strips on the breadboard
4. Connect one of the arduino's GND pins to the negative(-) bus strip of the bread board
5. Connect the brown/ground wire of the servos to the negative(-) bus strip of the bread board
6. Connect the red wire/power input(vcc) wire of the servos to the positive(+) bus strip of the bread board
7. Connect the orange/signal input wire of servo1 to the pin 3 on the Arduino
8. Connect the orange/signal input wire of servo2 to the pin 4 on the Arduino
9. Connect the orange/signal input wire of servo3 to the pin 7 on the Arduino
10. Connect the orange/signal input wire of servo4 to the pin 9 on the Arduino

# Configuration

Clone the repo:

git clone https://github.com/CH4RM-YT/3dof-Robotic-arm-to-sort-items-based-on-color.git

cd codes

pip install -r requirements.txt

Open the arm_movement.ino in your Arduino IDE and connect your Arduino UNO 

Check the com port your arduino is connected to, check this link for help(https://support.arduino.cc/hc/en-us/articles/4406856349970-Select-board-and-port-in-Arduino-IDE#:~:text=Select%20port%20with%20Tools%20%3E%20Port&text=In%20IDE%202%2C%20the%20Tools,dev/ttyACM0%20(Arduino%20Uno)

Replace COM8 in "arduino = serial.Serial('COM8', 9600, timeout=1)" with the yours, in the color_identifier.py file

Compile and upload the arduino code to your Arduino UNO 

Run color_identifier.py script

# Usage

hold a red or green colored item over your camera and watch the arm move
