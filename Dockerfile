FROM python:3.10


RUN mkdir /apart_analyser

WORKDIR /apart_analyser

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--reload"]
