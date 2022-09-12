FROM nikolaik/python-nodejs:latest

WORKDIR /app
RUN npm install -g serverless && npm install -g serverless-offline
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt 
COPY startup.sh /app/startup.sh
RUN chmod 777 /app/startup.sh
EXPOSE 3000
ENTRYPOINT ["/bin/sh", "/app/startup.sh"]


