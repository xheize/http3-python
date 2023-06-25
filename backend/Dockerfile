FROM python:3.10.10-alpine3.17

RUN apk add \
    openssl-dev\
    python3-dev \
    bsd-compat-headers\
    libffi-dev

RUN pip install -r requirements.txt

CMD ["python","main.py"]