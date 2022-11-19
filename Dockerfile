FROM python:alpine3.16

LABEL name=SSLCheck
LABEL author=gcdd1993

WORKDIR /scripts
COPY requirements.txt requirements.txt

RUN set -ex; \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install -r requirements.txt

COPY . .
CMD ["python", "/scripts/Launcher.py"]