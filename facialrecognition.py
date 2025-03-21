import cv2
import os
from deepface import DeepFace

# Path to the image database
image_database_path = "image_database"

# Load all images from the database
known_faces = {}
for filename in os.listdir(image_database_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(image_database_path, filename)
        known_faces[filename] = image_path

# Initialize video capture
cap = cv2.VideoCapture(0)

# Check if the camera is opened correctly
if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

# Loop to continuously capture frames from the webcam
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Display the resulting frame
    cv2.imshow('Live Video - Press Q to quit', frame)

    # Try to detect faces in the current frame
    try:
        # Analyze the frame to find faces
        faces = DeepFace.find(frame, db_path=image_database_path, model_name="VGG-Face", enforce_detection=False)

        if len(faces) > 0:
            for face in faces:
                # Retrieve the image name from the result
                recognized_face = face['identity']
                print(f"Recognized Face: {recognized_face}")
                cv2.putText(frame, f'Found: {recognized_face}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    except Exception as e:
        print(f"Error in face detection: {str(e)}")

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the windows
cap.release()
cv2.destroyAllWindows()
