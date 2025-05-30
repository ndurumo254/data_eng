from confluent_kafka import Producer
import json
import uuid
import random
import datetime
import time

# Kafka topics
VEHICLE_TOPIC = 'vehicle_data'
GPS_TOPIC = 'gps_data'
EMERGENCY_TOPIC = 'emergency_alerts'
WEATHER_TOPIC = 'weather_data'

# Starting and destination locations
start_location = {
    'latitude': 47.6600,   # Konstanz
    'longitude': 9.1750
}
destination_location = {
    'latitude': 48.7758,   # Stuttgart
    'longitude': 9.1829
}

# Number of steps in the journey
TOTAL_STEPS = 100
current_step = 0

# Calculate per-step increments
LATITUDE_INCREMENT = (destination_location['latitude'] - start_location['latitude']) / TOTAL_STEPS
LONGITUDE_INCREMENT = (destination_location['longitude'] - start_location['longitude']) / TOTAL_STEPS

def get_next_time():
    return datetime.datetime.utcnow()

def simulate_vehicle_movement():
    global start_location, current_step
    if current_step < TOTAL_STEPS:
        start_location['latitude'] += LATITUDE_INCREMENT + random.uniform(-0.0003, 0.0003)
        start_location['longitude'] += LONGITUDE_INCREMENT + random.uniform(-0.0003, 0.0003)
        current_step += 1
    return {
        'latitude': round(start_location['latitude'], 6),
        'longitude': round(start_location['longitude'], 6)
    }

def generate_vehicle_data(device_id):
    location = simulate_vehicle_movement()
    timestamp = get_next_time().isoformat()
    return {
        'id': str(uuid.uuid4()),
        'deviceId': device_id,
        'timestamp': timestamp,
        'latitude': location['latitude'],
        'longitude': location['longitude'],
        'speed': round(random.uniform(10, 40), 2),
        'direction': 'North-East',
        'make': 'BMW',
        'model': 'C500',
        'year': 2024,
        'fuelType': 'Hybrid'
    }

def generate_gps_data(device_id, vehicle_type='private'):
    location = simulate_vehicle_movement()
    timestamp = get_next_time().isoformat()
    return {
        'id': str(uuid.uuid4()),
        'deviceId': device_id,
        'timestamp': timestamp,
        'latitude': location['latitude'],
        'longitude': location['longitude'],
        'speed': round(random.uniform(10, 40), 2),
        'direction': 'North-East',
        'vehicleType': vehicle_type
    }

def generate_emergency_alert():
    timestamp = get_next_time().isoformat()
    alert_types = ['Accident', 'Fire', 'Flood', 'Roadblock']
    return {
        'id': str(uuid.uuid4()),
        'timestamp': timestamp,
        'type': random.choice(alert_types),
        'severity': random.choice(['Low', 'Medium', 'High']),
        'description': 'Emergency alert issued in the area.',
        'location': simulate_vehicle_movement()
    }

def fetch_weather_data():
    timestamp = get_next_time().isoformat()
    return {
        'id': str(uuid.uuid4()),
        'timestamp': timestamp,
        'temperature': round(random.uniform(-5, 35), 1),
        'humidity': round(random.uniform(30, 90), 1),
        'condition': random.choice(['Sunny', 'Cloudy', 'Rain', 'Snow']),
        'location': simulate_vehicle_movement()
    }

def send_vehicle_data(producer, device_id):
    data = generate_vehicle_data(device_id)
    producer.produce(VEHICLE_TOPIC, key=device_id, value=json.dumps(data))
    print(f"🚗 Vehicle Data: {data}")

def send_gps_data(producer, device_id):
    data = generate_gps_data(device_id)
    producer.produce(GPS_TOPIC, key=device_id, value=json.dumps(data))
    print(f"📍 GPS Data: {data}")

def send_emergency_alert(producer):
    data = generate_emergency_alert()
    producer.produce(EMERGENCY_TOPIC, key=str(data['id']), value=json.dumps(data))
    print(f"🚨 Emergency Alert: {data}")

def send_weather_data(producer):
    data = fetch_weather_data()
    producer.produce(WEATHER_TOPIC, key=str(data['id']), value=json.dumps(data))
    print(f"🌤️ Weather Data: {data}")

def simulate_journey(producer, device_id, iterations=100):
    for _ in range(iterations):
        send_vehicle_data(producer, device_id)
        send_gps_data(producer, device_id)
        if random.random() < 0.2:  # Occasionally send emergency alerts
            send_emergency_alert(producer)
        if random.random() < 0.5:  # Occasionally send weather updates
            send_weather_data(producer)
        producer.flush()
        time.sleep(1)

if __name__ == "__main__":
    producer_config = {
        'bootstrap.servers': 'localhost:9092',
        'error_cb': lambda err: print(f'Kafka error: {err}')
    }

    producer = Producer(producer_config)
    simulate_journey(producer, device_id="device-001", iterations=TOTAL_STEPS)
