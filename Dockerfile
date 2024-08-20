FROM python:3.11.5

WORKDIR /app

COPY builder/requirements.txt /app/
RUN pip install -r requirements.txt

COPY src/ /app/src/

CMD [ "python", "-u", "/app/src/handler.py" ]
