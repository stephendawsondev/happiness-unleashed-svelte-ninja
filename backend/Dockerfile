FROM python:3.9.17

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["gunicorn", "--bind", "0.0.0.0:8001", "happiness_unleashed.wsgi:application"]
