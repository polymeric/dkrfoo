FROM python:2.7
ADD . /dkrsrv
WORKDIR /dkrsrv
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["src/app.py"]
