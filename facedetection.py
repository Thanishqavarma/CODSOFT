import cv2

# Load face detection model
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Start webcam
camera = cv2.VideoCapture(0)

while True:

    # Read camera frame
    success, frame = camera.read()

    # Convert to gray color
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40)
    )

    # Draw rectangle around face
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

        cv2.putText(
            frame,
            "Face Detected",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # Show output window
    cv2.imshow("Face Detection AI", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()

cv2.destroyAllWindows()
