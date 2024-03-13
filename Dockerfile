FROM python:3.10

WORKDIR /Python-Oc-Lettings-FR 

COPY requirements.txt /Python-Oc-Lettings-FR/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . /Python-Oc-Lettings-FR/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

