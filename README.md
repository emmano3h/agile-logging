# AgileLogging #

AgileLogging is a practical streaming data infrastructure case.

### What is this repository for? ###

This repo is a stack to have running :
    1. Fluentd : Distributed logs platform system. Used with a connector (@type kafka2) to send logs in Kafka.
    2. Zookeeper : Distributed data management system. Used by Kafka.
    3. Kafka : Distributed messaging system. Mainly used because it is very scalable to produce and consume data.
    4. Kafka Connect : Used to easily connect to kafka and send data in ELasticsearch using connector "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector"
    5. kafka-connect-ui : Used to have acces to Kafka Connect using UI. You can use it to set up connector without go on command.
    6. Elasticsearch : Distributed logs database system. Used to index data and easily perform requests.
    7. Kibana : Ui to view data or logs stored in Elasticsearch
    


### How do I get set up? ###
* Dependencies
   - Docker

* Deployment instructions
    - Go in the stack folder: $ cd agile-logging 
    - Run the command : $  docker-compose -f docker-compose-dist-logging.yaml up --build --d
    - Waiting until all services started.
    - Check services running using docker ps or docker logs 'service_name' -f
    - Start a connector on kafka connector. It will be responsible to sync data from kafka to elasticsearch
        You have 2 possibilities to start connector:
        1. Using the command:
            $ docker exec -it kafka_connect bash 
            if you want to send data in elasticsearch on the same server*
                $ curl -X POST -H "Content-Type: application/json" --data @/opt/connector_conf/connector_elasticsearch.json http://localhost:8083/connectors>> 
            if you want to send data in S3*
                $ curl -X POST -H "Content-Type: application/json" --data @/opt/connector_conf/connector_s3.json http://localhost:8083/connectors
        
        2. Using the Kafka-connect UI if you kept it in the stack
            Open your browser and enter the url localhost:8003
            Create new sync
            Fill the json like:
            {  
               "name":"elasticsearch-sink",
               "config":{  
               "connector.class":"io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
               "tasks.max":"1",
               "topics":"log-messages",
               "key.ignore":"true",
               "schema.ignore": "true",
               "connection.url": "http://elasticsearch-agile-one:9200",
               "type.name": "kafka-connect"
            }
        }

### Possible performance optimizations for the Code. ###
    - Add more Zookeeper and Kafka nodes.
### Who do I talk to? ###

* Repo owner or admin
Full name: Emmanuel HODONOU 
Mail: emmano3h@gmail.com 
Github: https://github.com/emmano3h/