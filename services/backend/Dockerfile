# Section1: Base Image
FROM python:3.9

# Section2: Python Interpreter Flags

# ensures that the python output is sent straight to terminal (e.g. your container log)
# without being first buffered and that you can see the output of your application (e.g. django logs)
# in real time. Equivalent to python -u: https://docs.python.org/3/using/cmdline.html#cmdoption-u
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV TESTING 0

# Section3: Compiler and OS libraries
ENV TZ Asia/Shanghai

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
RUN echo $TZ > /etc/timezone
RUN sed -i -e 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN apt update && apt install -y locales tzdata
RUN dpkg-reconfigure -f noninteractive tzdata
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.UTF-8

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

# Section4: Project libraries and User Creation
COPY ./requirements.txt /tmp/requirements.txt

RUN pip3 install -U -i https://mirrors.aliyun.com/pypi/simple/ pip \
    && pip3 install -U -i https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

# Section5: Code and User Setup

## for migrations
COPY migrations .
COPY pyproject.toml .

COPY src/ .

