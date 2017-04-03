FROM python:onbuild
ADD . /code
WORKDIR /code
#RUN pip install -r requirements.txt
CMD ["python", "run.py"]
EXPOSE 5000
VOLUME /code
