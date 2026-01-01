
FROM python:3.9-slim


WORKDIR /app


COPY display_record.py .
COPY housing.csv .

CMD ["python", "display_record.py"]
