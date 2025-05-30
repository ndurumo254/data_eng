from confluent_kafka import Producer
import json
import uuid
import random
import datetime

# Kafka topics
VEHICLE_TOPIC = 'vehicle_data'
GPS_TOPIC = 'gps_data'

# Starting location
start_location = {
    'latitude': 52.5200,
    'longitude': 13.4050
}
LATITUDE_INCREMENT = 0.0001
LONGITUDE_INCREMENT = 0.0001

def get_next_time():
    return datetime.datetime.utcnow()

def simulate_vehicle_movement():
    global start_location
    start_location['latitude'] += LATITUDE_INCREMENT + random.uniform(-0.0003, 0.0003)
    start_location['longitude'] += LONGITUDE_INCREMENT + random.uniform(-0.0003, 0.0003)
    return {
        'latitude': round(start_location['latitude'], 6),
        'longitude': round(start_location['longitude'], 6)
    }

def generate_vehicle_data(device_id,vehicle_type ='private'):
    location = simulate_vehicle_movement()
    timestamp = get_next_time().isoformat()
    
    return {
        'vehicle': {
            'id': str(uuid.uuid4()),
            'deviceId': device_id,
            'timestamp': timestamp,
            'latitude': location['latitude'],
            'longitude': location['longitude'],
            'speed': round(random.uniform(10, 40), 2),
            'direction': random.choice(['North', 'South', 'East', 'West', 'North-East', 'South-West']),
            'make': 'BMW',
            'model': 'C500',
            'year': 2024,
            'fuelType': 'Hybrid'
        },
        'gps': {
            'id': str(uuid.uuid4()),
            'deviceId': device_id,
            'timestamp': timestamp,
            'latitude': location['latitude'],
            'longitude': location['longitude'], 
            'speed': random.uniform(a=0, b=40),  # km/h
            'direction': 'North-East',
            'vehicleType': vehicle_type ,   
            'speed': round(random.uniform(10, 40), 2),  # km/h
            'direction': 'North-East',
        }
    }

def simulate_journey(producer, device_id, iterations=5):
    for _ in range(iterations):
        data = generate_vehicle_data(device_id)

        vehicle_data = json.dumps(data['vehicle'])
        gps_data = json.dumps(data['gps'])

        # Send to respective Kafka topics
        producer.produce(VEHICLE_TOPIC, key=device_id, value=vehicle_data)
        producer.produce(GPS_TOPIC, key=device_id, value=gps_data)

        print("Sent to Kafka:")
        print("Vehicle data:", data['vehicle'])
        print("GPS data:", data['gps'])

        producer.flush()

if __name__ == "__main__":
    producer_config = {
        'bootstrap.servers': 'localhost:9092',
        'error_cb': lambda err: print(f'Kafka error: {err}')
    }

    producer = Producer(producer_config)
    simulate_journey(producer, device_id="device-001", iterations=5)
