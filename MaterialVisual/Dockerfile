FROM python:3.7-buster

#ARG COMPILEALL

RUN echo "deb https://mirrors.aliyun.com/debian/ buster main contrib non-free" > /etc/apt/sources.list && \
    echo "deb https://mirrors.aliyun.com/debian/ buster-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.aliyun.com/debian/ buster-backports main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.aliyun.com/debian-security/ buster/updates main contrib non-free" >> /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y gcc libc-dev nginx libsasl2-dev libldap2-dev libssl-dev zip jq postgresql-11 && \
    apt-get clean

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

RUN mkdir /app

COPY . /app/
RUN cp -f /app/uwsgi/default /etc/nginx/sites-enabled/

RUN pip install --no-cache --upgrade -i https://mirrors.aliyun.com/pypi/simple pip && \
    pip install --no-cache --timeout=120 -i https://mirrors.aliyun.com/pypi/simple -r /app/requirements.txt

WORKDIR /app

#RUN if $COMPILEALL; then python3 -m compileall . -f -b -x "manage.py" && find . -mindepth 2 -name "*.py" -exec rm {} \;; fi

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
