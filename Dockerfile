# pull official base image
FROM python:3.9.6-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install system dependencies
RUN apk update \
    && apk add --no-cache postgresql-dev gcc python3-dev musl-dev \
    && rm -rf /var/cache/apk/*


# install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run the Django development server
CMD ["sh", "-c", "./entrypoint.sh && python manage.py runserver 0.0.0.0:8000"]

