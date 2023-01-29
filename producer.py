from kafka import KafkaProducer
from const import *
import sys

# try:
#     topic = sys.argv[1]
# except:
#     print ('Usage: python3 producer <topic_name>')
#     exit(1)
    
producer = KafkaProducer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])
topico = ['even', 'odd'];
for i in range(100):
    if i % 2 == 0:
        msg = 'Number ' + str(i) + 'st message for topic ' + topico[0]
        print('Sending message: ' + msg)
        producer.send(topico[0], value=msg.encode())
    else:
        msg = 'Number ' + str(i) + 'st message for topic ' + topico[1]
        print('Sending message: ' + msg)
        producer.send(topico[1], value=msg.encode())

producer.flush()
