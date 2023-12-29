FROM python:3.10.6
RUN pip install --upgrade pip
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
RUN pip install -r ./requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog_proj.wsgi:application"]