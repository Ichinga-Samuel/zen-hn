FROM python:3.12-alpine

LABEL author="Ichinga Samuel"

WORKDIR /zen_hn

COPY requirements.txt /zen_hn

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir -r requirements.txt

COPY . /zen_hn

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
