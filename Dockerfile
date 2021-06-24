FROM python:3.7-alpine
WORKDIR /cartwheel
COPY . /
CMD ["cartwheel.py"]
ENTRYPOINT ["python3"]
