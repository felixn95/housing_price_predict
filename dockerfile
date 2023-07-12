FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app

COPY ./app /app
COPY ./gradio /app/gradio
COPY ./requirements.txt /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
