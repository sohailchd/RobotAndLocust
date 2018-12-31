
FROM python:3-onbuild

COPY .  /usr/src/app/

RUN ls -la /

RUN apt-get update && apt-get install -yq \
    chromium \
    git-core \
    firefox-esr \
    xvfb \
    xsel \
    unzip \
    python-pytest \
    libgconf2-4 \
    libncurses5 \
    libxml2-dev \
    libxslt-dev \
    libz-dev \
    xclip \
    libfontconfig1 \
    libglib2.0-0 \
    libnss3 \
    libfontconfig1


# Install Chrome for Selenium
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb
RUN dpkg -i /chrome.deb || apt-get install -yf
RUN rm /chrome.deb


RUN ["chmod", "+x","/usr/src/app/robot_runner.sh"]
ENTRYPOINT ["/usr/src/app/robot_runner.sh"]
CMD []