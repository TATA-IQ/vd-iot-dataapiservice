# Introduction 
This is a data api service repo. 



# Architecture
![Architectural Flow](abc.png)

1. This module is hosted using uvicorn with multiple workers
2. FastAPI receives HTTP requests and each worker process the request
3. This module uses multiple workers to process for managing incoming multiple requests
4. After processing, an output is sentout as response json
# Dependency
1. MySQL Database: Stores configuration and processing data for various levels such as camera configurations, preprocessing, postprocessing, and scheduling managements.

# Installation
1. Install Python3.9 
3. poetry install

# Run App
uvicorn fastapp:app --host=0.0.0.0 --port=8051 --workers=5

# Docker 
1. Containarization is enabled
2. change the config.yaml
2. Navigate to the Dockerfile level
2. build the container (sudo docker build -t "dataapi" .)
3. Run the container (sudo docker run -t "dataapi")