FROM python:3.9

WORKDIR /src

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

COPY . /src

RUN pip install --no-cache-dir opencv-contrib-python

ENV DISPLAY=:0
ENV QT_X11_NO_MITSHM=1

CMD ["python", "src/main.py"]
