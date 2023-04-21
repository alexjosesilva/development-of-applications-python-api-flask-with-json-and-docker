# syntax=docker/dockerfile:1

FROM python:3.10.8
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
# Add this:
ENV FLASK_APP=src/app.py
ENV FLASK_DEBUG=1

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]