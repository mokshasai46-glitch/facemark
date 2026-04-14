import cv2
import requests

# Flask server URL
ENROLL_URL = "http://127.0.0.1:5000/enroll"
ATTENDANCE_URL = "http://127.0.0.1:5000/attendance"

def capture_and_send(endpoint, student_id=None, session_id=None):
    cap = cv2.VideoCapture(0)  # 0 = default webcam
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Failed to capture image")
        return

    # Save temporary image
    cv2.imwrite("temp.jpg", frame)

    files = {"image": open("temp.jpg", "rb")}
    data = {}
    if student_id:
        data["student_id"] = student_id
    if session_id:
        data["session_id"] = session_id

    response = requests.post(endpoint, files=files, data=data)
    print(response.json())

# Example usage:
# Enroll student
if __name__ == "__main__":
    choice = input("Enter 'e' to enroll or 'a' to mark attendance: ")
    if choice == 'e':
        student_id = input("Enter student ID: ")
        capture_and_send(ENROLL_URL, student_id=student_id)
    elif choice == 'a':
        session_id = input("Enter session ID: ")
        capture_and_send(ATTENDANCE_URL, session_id=session_id)
    else:
        print("Invalid choice")
