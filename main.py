import cv2
from flask import * 

app = Flask(__name__)


@app.route('/')
def home(): 
    return render_template('home.html')

camera = cv2.VideoCapture(0)
def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 

# @app.route('/capture')
# def capture(): 
    # cap = cv2.VideoCapture(0)
    # ok_flag = True
    # while ok_flag: 
    #     ret, frame = cap.read()
    #     cv2.imshow('my Window', frame)
    #     if cv2.waitKey(0) == "q": 
    #         ok_flag = False


    # cv2.destroyAllWindows()
    # cap.release()    
        
#     return response()


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__": 
    app.run(debug = True)