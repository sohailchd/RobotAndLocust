FROM python:3-onbuild
COPY . /usr/src/rest_api
RUN ["chmod", "+x","/usr/src/rest_api/pytest_api/execute_api.sh"]
CMD ["/usr/src/rest_api/pytest_api/execute_api.sh"]