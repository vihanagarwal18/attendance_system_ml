import cv2
import os

# Take the name of the person as input
person_name = input("Enter the name of the person: ")

# Create a folder with the person's name to store images
folder_name = os.path.join('captured_images', person_name)
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Open the camera
cap = cv2.VideoCapture(0)  # 0 for default camera, you can change this if needed

saving = False  # Flag to indicate whether we are saving images or not
count = 1  # Counter for saved images

while True:
    ret, frame = cap.read()
    cv2.imshow('Capture', frame)
    
    # Start saving images when 's' is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        saving = True
    
    if saving:
        img_name = os.path.join(folder_name, f'image_{count}.jpg')
        cv2.imwrite(img_name, frame)
        print(f'Saved: {img_name}')
        count += 1

    # Stop saving images when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
