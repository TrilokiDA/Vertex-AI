FROM gcr.io/deeplearning-platform-release/tf-gpu.2-6
# FROM gcr.io/deeplearning-platform-release/tf2-cpu.2-6
# FROM gcr.io/google-appengine/python
WORKDIR /
COPY . /


RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]