FROM tiangolo/uvicorn-gunicorn:python3.7
ARG POSTGRES_URL
ENV POSTGRES_URL "${POSTGRES_URL:-localhost:5432/}"

ADD requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /app/

WORKDIR /app/

ADD src ./src/
ADD main.py ./main.py