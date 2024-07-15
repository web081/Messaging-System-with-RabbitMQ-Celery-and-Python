## Messaging System with RabbitMQ/Celery and Python

### Deploy a Python application behind Nginx that interacts with RabbitMQ/Celery for email sending and logging functionality.

#### Install RabbitMQ and Celery on your local machine:
```sh
sudo apt-get update
sudo apt-get install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
```

### Celery Installation

```sh
pip install celery
```

