FROM python:3.9-slim
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install mysql-connector-python
RUN pip install pandas
RUN pip install opencv-python
RUN pip install requests
RUN pip install imutils
RUN pip install fastapi==0.99.1
RUN pip install "uvicorn[standard]"
RUN pip install protobuf==3.20.*
RUN pip install python-consul
copy dataapiservice /app
WORKDIR /app
# RUN mkdir /app/logs
CMD ["uvicorn", "fastapp:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "5"]