FROM python:3-onbuild
COPY . /usr/src/load_test
RUN ["chmod", "+x","/usr/src/load_test/load_runner.sh"]
CMD ["/usr/src/load_test/load_runner.sh"]