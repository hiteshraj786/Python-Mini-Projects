import cv2
# Load the pre-trained face detection model
face_cap = cv2.CascadeClassifier("C:/Users/hites/AppData/Local/Programs/Python/Python313/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# Open webcam
video_cap = cv2.VideoCapture(0)
while True:
   
    ret , video_data = video_cap.read()


    if not ret:
        break
    
       # Convert to grayscale

    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

       # Face detection
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

      # Draw rectangles
    for(x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)


     # Show the video frame with face detection
    cv2.imshow("video_live",video_data)


        # Press 'a' to break
    if cv2.waitKey(10) == ord("a"):
        break
# Release and close
video_cap.release()
cv2.destroyAllWindows()

