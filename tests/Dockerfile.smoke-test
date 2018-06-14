FROM python:2.7
WORKDIR /dkrtest
EXPOSE 5000
COPY . /dkrtest
RUN pip install --no-cache-dir -r requirements.txt
CMD ["py.test", "-v", "test_rest_api.py"]
