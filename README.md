#Check available data in the kafika topic
docker exec -it kafka-broker bash


#list Topics
kafka-topics --bootstrap-server localhost:9092 --list


#car_topic
kafka-console-consumer --bootstrap-server localhost:9092 --topic vehicle_data --from-beginning
