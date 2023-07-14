FROM nvidia/cuda:12.0.1-base-ubuntu22.04

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y software-properties-common && \
    apt-get install python3.10 -y && \
    apt-get install python3-pip -y

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "api_server.py"]