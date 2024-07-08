from square.client import Client

def list_square_locations():
    client = Client(
        access_token="1234567890abcdef1234567890abcdef",
        environment='sandbox'  # Use 'production' for live environment
    )

    result = client.locations.list_locations()

    if result.is_success():
        for location in result.body['locations']:
            print(f"ID: {location['id']}, Name: {location['name']}")
    elif result.is_error():
        for error in result.errors:
            print(f"Error: {error['category']}, Code: {error['code']}, Detail: {error['detail']}")
