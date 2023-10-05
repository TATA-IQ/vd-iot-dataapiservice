import cv2
import fastapi
import json
import base64
import imutils
from datetime import datetime

class GetCameraFrames():
    def get_data(rtsp_url, username, password,logger=None):
        """
        Retrieves camera frames from the given RTSP URL using the provided credentials.

        Args:
            rtsp_url (str): The RTSP URL of the camera stream.
            username (str): Username of the camera.
            password (str): Password of the camera.
            logger: (Optional).

        Returns:
            FastAPI JSONResponse which contains base64 encoded camera frames.
        """
        rtsp_url_cam = f'rtsp://{username}:{password}@{rtsp_url}'
        cap = cv2.VideoCapture(rtsp_url_cam,cv2.CAP_FFMPEG)
        fps = cap.get(cv2.CAP_PROP_FPS)
        interval = 5 # provide how many frames per second are needed 
        frame_interval = int(fps/interval)
        frame_count = 0
        while True:
            ret,frame = cap.read()
            fname = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")+".jpg"
            frame = imutils.resize(frame,width=640)
            if not ret:
                print("there are no frames, waiting for the frames")
                continue
            if frame_count % frame_interval==0:
                img_string = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode()  
                # cv2.imwrite()
            frame_count += 1
        cap.release()
        return fastapi.responses.JSONResponse(content={"data":img_string})
    
    def get_first_frame(rtsp_url, username, password,logger=None):
        """
        Retrieves only the first camera frame from the given RTSP URL using the provided credentials.

        Args:
            rtsp_url (str): The RTSP URL of the camera stream.
            username (str): Username of the camera.
            password (str): Password of the camera.
            logger: (Optional).

        Returns:
            FastAPI JSONResponse which contains base64 encoded first camera frame.
        """
        rtsp_url_cam = f'rtsp://{username}:{password}@{rtsp_url}'
        print(rtsp_url_cam)
        cap = cv2.VideoCapture(rtsp_url_cam,cv2.CAP_FFMPEG)
        ret,frame = cap.read()
        frame = imutils.resize(frame,width=640)
        img_string = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode()  
        cv2.imshow('Frame', frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        cap.release()
        return fastapi.responses.JSONResponse(content={"data":img_string})

    def create_url(url, username, password):
        if password is None:
            pass
        elif len(password)<=1:
           pass
        else:
            if "rtsp://" in url:
                url = url.replace("rtsp://", "")
                rtsplink = "rtsp://" + username + ":" + password + "@" + url  # noqa: E501
                url=rtsplink
            else:
                print(f"Unexpected Url Type for {url}")
        return url
    
    def get_desired_frames(rtsp_url, username, password,logger=None):
        """
        Retrieves the desired number of camera frames from the given RTSP URL using the provided credentials and
        by changing the desired fps and desired number of frames in the function.

        Args:
            rtsp_url (str): The RTSP URL of the camera stream.
            username (str): Username of the camera.
            password (str): Password of the camera.
            logger: (Optional).

        Returns:
            FastAPI JSONResponse which contains base64 desired number of camera frames.
        """
        # if username and password:
        #     rtsp_url_cam = f'rtsp://{username}:{password}@{rtsp_url}'
        # else:
        #     rtsp_url_cam = rtsp_url
        # print(rtsp_url_cam)
        rtsp_url_cam = GetCameraFrames.create_url(rtsp_url, username, password)
        print("rtsp_url_cam====",rtsp_url_cam)
        cap = cv2.VideoCapture(rtsp_url_cam,cv2.CAP_FFMPEG)
        camera_fps = cap.get(cv2.CAP_PROP_FPS)
        desired_fps = 5 # provide how many frames per second are needed 
        desired_frames = 1 # provide how many frames you need
        frame_interval = int(camera_fps/desired_fps)
        frame_count = 0
        output_count = 0
        try:
            while True:
                ret,frame = cap.read()
                height, width, channels = frame.shape
                frame = imutils.resize(frame,width=int(width*0.20))
                if not ret:
                    print("there are no frames, waiting for the frames")
                    continue
                    # return fastapi.responses.JSONResponse(content={"data":None}) 
                if frame_count % frame_interval==0:
                    fname = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")+".jpg"
                    #cv2.imwrite()
                    img_string = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode()  
                    # imgstr = img_string.encode('utf8')               
                    # img_string = cv2.imencode(".jpg", frame)[1].tobytes().decode("utf-8")
                    output_count += 1
                    if desired_frames is not None:
                        if output_count==desired_frames:
                            break
                frame_count += 1
            # cap.release()
        except Exception as e:
            print(e)
            return fastapi.responses.JSONResponse(content={"data":None,"status":0,"message":"couldn't connect to camera"})
        finally:
            cap.release()
            
        return fastapi.responses.JSONResponse(content={"data":img_string,"status":1,"message":"connected to camera"})