# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

This repo is a stack to have running :
    1- Fluentd : Distributed logs platform system. Used with a connector (@type kafka2) to send logs in Kafka.
    2- Zookeeper : Distributed data management system. Used by Kafka.
    3- Kafka : Distributed messaging system. Mainly used because it is very scalable to produce and consume data.
    4- Kafka Connect : Used to easily connect to kafka and send data in ELasticsearch using connector "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector"
    5- kafka-connect-ui : Used to have acces to Kafka Connect using UI. You can use it to set up connector without go on command.
    6- Elasticsearch : Distributed logs database system. Used to index data and easily perform requests.
    7- Kibana : Ui to view data or logs stored in Elasticsearch
    


### How do I get set up? ###
* Dependencies
   - Docker

* Deployment instructions
    - Go in the stack folder: $ cd agile-logging 
    - Run the command : $  docker-compose -f docker-compose-dist-logging.yaml up --build --d
    - Waiting until all services started.
    - Check services running using docker ps or docker logs 'service_name' -f
        

### Possible performance optimizations for the Code. ###
    - Add Zookeeper and Kafka nodes.
### Who do I talk to? ###

* Repo owner or admin
Full name: Emmanuel HODONOU 
Mail: emmano3h@gmail.com 
Github: https://github.com/emmano3h/