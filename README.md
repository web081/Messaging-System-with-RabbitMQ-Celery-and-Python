## Messaging System with RabbitMQ/Celery and Python

<b> I will develop a Python Messaging Queue testing system, a Python application behind Nginx that interacts with RabbitMQ/Celery for email sending and logging functionality which consists of the following 'Tools' as our requirement. </b>

- RabbitMQ
- Celery
- Ngrok
- Nginx

##### What is RabbitMQ?

RabbitMQ is an open-source messaging software that implements the Advanced Message Queuing Protocol (AMQP) and is widely used for managing messaging queues. 

##### What is Celery?

Celery is an asynchronous task/job queue based on distributed message passing. its main purpose is to handle "asynchronous" task queue/job queue that handles the execution of background tasks

##### What is Ngrok?

Ngrok is a tool that creates secure tunnels from a public endpoint (like the internet) to a locally running web service or application
##### 

#### Install RabbitMQ and Celery on your local machine:
```sh
sudo apt-get update
sudo apt-get install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
```

### Celery, Flask, python-dotenv Installation

```sh
pip install flask celery python-dotenv
```
#### Install Nginx server
```sh
apt-get install nginx
```
#### Install ngrok and expose the local server:
```sh
ngrok http 8080
```
### working dir tree of the file
```sh
messaging_system/
│
├── app.py
├── messaging_system.log
├── celery_worker.py
├── nginx.conf
├── requirements.txt
├── venv/

```
### Testing Endpoint to ensure the application is working properly
```sh
localhost:5000
localhost:5000/?sendmail=bomprince@gmail.com  #sending email endpoint
localhost:+5000/?talktome    
localhost:5000/logs       #testing retrieve logs endpoint
```
