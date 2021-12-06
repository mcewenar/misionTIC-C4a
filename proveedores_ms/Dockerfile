FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /users
WORKDIR /users
ADD . /users/
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT
























#Crear una imagen para correr de forma local:
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ARG URL=0.0.0.0:4000

#CMD ["sh", "-c", "python manage.py runserver $URL"]
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver $URL"]



#ejecutar docker run -p 4000:4000 -e URL=0.0.0.0:4000  auth_ms