FROM python:3.11.5

WORKDIR /app

ENV PYTHONPATH="/app/builder:/app/src"

COPY builder/ /app/builder/
COPY src/ /app/src/
COPY builder/requirements.txt /app/
RUN pip install -r requirements.txt

CMD ["python", "-u", "/app/src/handler.py"]