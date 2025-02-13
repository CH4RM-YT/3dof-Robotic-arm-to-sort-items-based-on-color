#include <Servo.h>

// Create servo objects for all 4 servos
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

// Define the servo pins
const int servo1Pin = 3;  // Servo 1 connected to digital PWM pin 3
const int servo2Pin = 4;  // Servo 2 connected to digital PWM pin 5
const int servo3Pin = 7;  // Servo 3 connected to digital PWM pin 6
const int servo4Pin = 9;  // Servo 4 connected to digital PWM pin 9

// Define the original position for Servo 1
const int originalpositionbase = 70;  // Center position (90 degrees)
const int originalpositionwrist = 70;
const int originalpositionelbow = 90;


// this part is only if you are using an mg90s continous rotation servo
void elbow() {
  servo2.write(0);
  servo2.detach();
  // delay(2000);
  returnToOriginalWrist();
  servo2.detach();
}


void wrist() {
  servo3.write(170);
  delay(2000);
  servo3.write(70);
  delay(5000);
}

// this part is only if you are using an mg90s continous rotation servo
//the gripper code
void grip() {
  servo4.attach(9);
  servo4.write(10);
  delay(300);
  servo4.detach();
}

// this part is only if you are using an mg90s continous rotation servo
void ungrip() {
  servo4.attach(9);
  servo4.writeMicroseconds(1800);  // Move back to 0°
  delay(1000);
  servo4.detach();
}

// Function to pick up and place red objects to the right
void red() {
  ungrip();
  delay(1000);
  servo2.write(156);
  delay(3000);
  servo3.write(140);
  delay(3000);
  grip();
  delay(3000);
  servo3.write(70);
  delay(3000);
  servo1.write(0);
  delay(3000);
  servo3.write(100);
  delay(3000);
  ungrip();
  delay(3000);
  returnToOriginalElbow();
  returnToOriginal();
  while (true);
}

// Function to pick up and place green objects to the left
void green() {
  ungrip();
  delay(1000);
  servo2.write(156);
  delay(3000);
  servo3.write(145);
  delay(3000);
  grip();
  delay(3000);
  servo3.write(70);
  delay(3000);
  servo1.write(140);
  delay(3000);      
  servo3.write(100);
  delay(2000);
  ungrip();
  delay(3000);
  returnToOriginalElbow();
  returnToOriginal();
  while (true);
}

// Function to return the arm to its original position
// you can modify it based on your requirements
void returnToOriginal() {
  servo1.write(originalpositionbase); 
  delay(3000);                     
}
void returnToOriginalWrist() {
  servo2.write(originalpositionwrist); 
  delay(3000);                     
}

void returnToOriginalElbow() {
  servo2.write(originalpositionelbow); 
  delay(3000);                     
}

void setup() {
  // Attach each servo to its respective pin
  servo1.attach(servo1Pin);
  servo2.attach(servo2Pin);
  servo3.attach(servo3Pin);
  servo4.attach(servo4Pin);

  // Initialize serial communication
  Serial.begin(9600);

  // Move the arm to its original position at startup
  returnToOriginal();
}

void loop() {
  // Check if data is available to read
  if (Serial.available() > 0) {
    // Read the incoming data
    String color = Serial.readString();
    color.trim();  // Remove any extra whitespace or newline characters

    // Call the appropriate function based on the received color
    if (color == "Red") {
      red();
    } else if (color == "Green") {
      green();
    }

    // Print the received color to the Serial Monitor
    Serial.print("Detected Color: ");
    Serial.println(color);
  }

  // you can uncomment the below functions to see the outcomes of each
  // grip();
  // ungrip();
  // green();
  // red();
  // wrist();
}