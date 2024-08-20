FROM python:3.11.5

WORKDIR /app

ENV PYTHONPATH=/app/builder

COPY builder/requirements.txt /app/
RUN pip install -r requirements.txt

COPY builder/ /app/builder/
COPY src/ /app/src/

CMD [ "python", "-u", "/app/src/handler.py" ]