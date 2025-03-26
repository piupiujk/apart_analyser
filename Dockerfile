FROM python:3.10

RUN mkdir /apart_analyser

WORKDIR /apart_analyser

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /apart_analyser/docker/app.sh

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
