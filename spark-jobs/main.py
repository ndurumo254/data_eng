import uuid
import random
import datetime
import json
from pprint import pprint

# Constants for simulation
LATITUDE_INCREMENT = 0.0001
LONGITUDE_INCREMENT = 0.0001

# Start location (e.g., near Birmingham)
start_location = {'latitude': 52.4862, 'longitude': -1.8904}


def get_next_time():
    return datetime.datetime.utcnow()


def simulate_vehicle_movement():
    global start_location
    # Move towards Birmingham (or any direction)
    start_location['latitude'] += LATITUDE_INCREMENT
    start_location['longitude'] += LONGITUDE_INCREMENT

    # Add randomness to simulate real movement
    start_location['latitude'] += random.uniform(-0.0005, 0.0005)
    start_location['longitude'] += random.uniform(-0.0005, 0.0005)

    return start_location


def generate_vehicle_data(device_id):
    location = simulate_vehicle_movement()
    return {
        'id': str(uuid.uuid4()),
        'deviceId': device_id,
        'timestamp': get_next_time().isoformat(),
        'location': (location['latitude'], location['longitude']),
        'speed': round(random.uniform(10, 40), 2),
        'direction': 'North-East',
        'make': 'BMW',
        'model': 'C500',
        'year': 2024,
        'fuelType': 'Hybrid'
    }


def simulate_journey(producer, device_id):
    while True:
        vehicle_data = generate_vehicle_data(device_id)
        pprint(vehicle_data)  # Or use print(json.dumps(...)) for JSON format
        break


if __name__ == "__main__":
    # Simulated Kafka producer config (not used in this example)
    producer_config = {
        'bootstrap.servers': 'localhost:9092',  # Example placeholder
        'error_cb': lambda err: print(f'Kafka error: {err}')
    }

    simulate_journey(producer=None, device_id="device-001")
