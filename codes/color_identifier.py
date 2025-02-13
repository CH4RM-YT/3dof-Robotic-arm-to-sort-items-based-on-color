import numpy as np
import cv2
import serial
import time

# Capturing video through webcam
webcam = cv2.VideoCapture(0)

# Function to send data to Arduino
def send_to_arduino(data):
    try:
        # Open the serial connection
        arduino = serial.Serial('COM8', 9600, timeout=1)
        time.sleep(2)  # Wait for the connection to establish
        # Send the data
        arduino.write(data.encode())
        print(f"Sent: {data}")
    except Exception as e:
        print(f"Error sending data to Arduino: {e}")
    finally:
        # Close the serial connection
        if 'arduino' in locals():
            arduino.close()
            time.sleep(1)  # Add a delay to ensure the port is released

# Variables for color detection delay
last_detection_time = 0  # Timestamp of the last color detection
detection_delay = 35     # Delay in seconds before detecting another color

# Start a while loop
while True:
    # Reading the video from the webcam in image frames
    ret, imageFrame = webcam.read()

    # Check if the frame was successfully captured
    if not ret:
        print("Failed to capture frame")
        break

    # Convert the imageFrame to HSV color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Calculate the average brightness of the frame
    grayFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2GRAY)
    average_brightness = np.mean(grayFrame)

    # If the frame is too dark, skip color detection
    if average_brightness < 50:  # Adjust this threshold as needed
        cv2.putText(imageFrame, "Low Light", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        cv2.imshow("Multiple Color Detection in Real-Time", imageFrame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        continue

    # Check if the detection delay has passed
    current_time = time.time()
    if current_time - last_detection_time < detection_delay:
        # Display the remaining delay time on the frame
        remaining_time = int(detection_delay - (current_time - last_detection_time))
        cv2.putText(imageFrame, f"Wait: {remaining_time}s for operation to end", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        cv2.imshow("Multiple Color Detection in Real-Time", imageFrame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        continue

    # Define color ranges and masks
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    # Adjusted blue range to avoid detecting dark areas
    blue_lower = np.array([100, 150, 50], np.uint8)  # Adjusted lower bound
    blue_upper = np.array([140, 255, 255], np.uint8)  # Adjusted upper bound
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    # Morphological Transform (Dilation)
    kernel = np.ones((5, 5), "uint8")

    red_mask = cv2.dilate(red_mask, kernel)
    green_mask = cv2.dilate(green_mask, kernel)
    blue_mask = cv2.dilate(blue_mask, kernel)

    # Find contours for each color
    def get_largest_contour(mask):
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            return max(contours, key=cv2.contourArea)  # Return the largest contour
        return None

    # Get the largest contour for each color
    red_contour = get_largest_contour(red_mask)
    green_contour = get_largest_contour(green_mask)
    blue_contour = get_largest_contour(blue_mask)

    # Determine which color has the largest contour
    detected_color = None
    largest_area = 0
    if red_contour is not None:
        area = cv2.contourArea(red_contour)
        if area > largest_area:
            largest_area = area
            detected_color = ("Red", red_contour, (0, 0, 255))
    if green_contour is not None:
        area = cv2.contourArea(green_contour)
        if area > largest_area:
            largest_area = area
            detected_color = ("Green", green_contour, (0, 255, 0))
    if blue_contour is not None:
        area = cv2.contourArea(blue_contour)
        if area > largest_area:
            largest_area = area
            detected_color = ("Blue", blue_contour, (255, 0, 0))

    # Draw the largest contour and send the detected color to Arduino
    if detected_color is not None:
        color_name, contour, color_bgr = detected_color
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(imageFrame, (x, y), (x + w, y + h), color_bgr, 2)
        cv2.putText(imageFrame, f"{color_name} Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color_bgr)
        send_to_arduino(color_name)
        # Update the last detection time
        last_detection_time = time.time()

    # Display the output
    cv2.imshow("Multiple Color Detection in Real-Time", imageFrame)

    # Exit on 'q' key press
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release resources
webcam.release()
cv2.destroyAllWindows()