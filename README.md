# AgileLogging #

AgileLogging is a practical streaming data infrastructure case.

### About ###

This repo is a stack to have running :
1. [Fluentd](https://https://www.fluentd.org/) : An open source data collector for unified logging layer. I used a connector (@type kafka2) to send logs in Kafka.
2. [Kafka](https://www.confluent.io/) : Distributed streaming platform. Fluentd produces data in Kafka.
3. [Zookeeper](https://zookeeper.apache.org/) : Kafka run with Zookeeper. Zookeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. 
4. [Kafka Connect](https://zookeeper.apache.org/) : an component of Kafka, is a framework for connecting Kafka with external systems such as databases, key-value stores, search indexes, and file systems. It is used here to easily connect to kafka and send data in Elasticsearch. I used the [Kafka Connect ElasticSearch ](https://docs.confluent.io/current/connect/kafka-connect-elasticsearch/index.html)
5. [kafka-connect-ui](https://hub.docker.com/r/landoop/kafka-connect-ui) : Used to have access to Kafka Connect UI. I used it to set up connector without go on command line.
6. [Elasticsearch](https://www.elastic.co/) : It is an distributed platform and a RESTful search and analytics engine. Used here to index and easily search data.
7. [Kibana](https://www.elastic.co/) : UI to connect and view data or logs stored in Elasticsearch.
8. python-app-test : A Python application to test the logs streaming.

### How do you get set up? ###
* Dependencies
   - Docker

* Deployment instructions
    - Open your terminal 
    - Go in the stack folder: 
        `$ cd agile-logging `
    - Run the docker-compose and wait until services started: 
        `$  docker-compose -f docker-compose-dist-logging.yaml up --build --d`
    - After all services created, check services running:
        `$ docker ps`
        You should see the following services unordered running:
        . python-app-test
        . fluentd-agile
        . zookeeper-agile-node1
        . kafka-agile-node1
        . kafka_connect
        . kafka-connect-ui
        . elasticsearch-agile-one
        . kibana-agile
    - Start a connector on kafka connector. It will be responsible to consume data from kafka and sync it in elasticsearch
        You have 2 possibilities to start connector:
        
        1. Using the command :
           Enter in the docker 
               `$ docker exec -it kafka_connect bash`
           Inside the docker, add the the connector by running the following command
               `$ curl -X POST -H "Content-Type: application/json" --data @/opt/connector_conf/connector_elasticsearch.json http://localhost:8083/connectors`
               
               You will see an output like the following. It means that your connector has been added  :
               `{
                   {
                       "name":"elasticsearch-sink",
                       "config":{"connector.class":"io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
                       "tasks.max":"1",
                       "topics":"log-messages",
                       "key.ignore":"true",
                       "schema.ignore":"true",
                       "connection.url":"http://elasticsearch-agile-one:9200",
                       "type.name":"kafka-connect",
                       "name":"elasticsearch-sink"
                   },
                   "tasks":[],
                   "type":null
               }`
               
        
        2. Using the Kafka-connect UI 
            Open your browser and go on http://localhost:8003
            Click on the button "New" to add new connector
            Choose ElasticSearch Connector and fill json like in the file located here connector_conf/connector_elasticsearch.json
            `{  
               "name":"elasticsearch-sink",
               "config":{  
               "connector.class":"io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
               "tasks.max":"1",
               "topics":"log-messages",
               "key.ignore":"true",
               "schema.ignore": "true",
               "connection.url": "http://elasticsearch-agile-one:9200",
               "type.name": "kafka-connect"
            }`
            
           Click on the button "create" when you finish. 
            
    - Open your browser and go on http://localhost:8003. You should see the count of _****SINK CONNECTORS****_ at 1. It means connectors has been added.
    - Let's check now with Kibana if the connector has created our indice in Elasticsearch. 
        . Open your browser and go on http://localhost:5601/
        . Find "Management" menu and click on it
        . Under Elasticsearch section, click on "Index Management" and you should see your indice created with the name "log-messages"
        . To visualize data with Kibana, we should create an index pattern. 
            So under Kibana section, click on "Index Patterns" and click on "Create index pattern". Fill the index pattern name "log-messages*" and click on "next step" and finish
        . Indexpattern created now, go in the left menu and click on "Discover" link to already view some data after selecting the index "log-messages".
    - Open your browser and go on http://localhost:7500/v1/organization and you will see the application output:
        
        `{"result": "Wow! !:)"}`
        
        Go on Kibana and refresh data to see your logs data there.
        Hit again http://localhost:7500/v1/organization and go to view changes in Kibana 

### Possible performance optimizations for the Code. ###
    - This is a proof of concept. To scale the system we can add more Zookeeper and Kafka nodes.
### Who do you talk to? ###

*   Repo owner or admin
    Full name: Emmanuel HODONOU 
    Mail: emmano3h@gmail.com 
    Github: https://github.com/emmano3h/