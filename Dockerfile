FROM python:3

LABEL maintainer "ckyOL <dev@ckyol.moe>"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-u", "./start.py" ]