FROM python:3.9.7
ADD . /app
WORKDIR /app
RUN pip install --upgrade setuptools
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirement.txt
EXPOSE 5000
CMD ["python", "app.py"]