FROM python:3
RUN pip install paho-mqtt
RUN pip install pyserial
RUN pip install requests
WORKDIR /app
COPY no_app /no_app
ENTRYPOINT ["python"]
CMD ["/no_app/none.py"]
