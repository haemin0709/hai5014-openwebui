import requests
import json

def get_latest_shuttle_bus_location():
    """
    Fetches the shuttle bus location data for Sungkyunkwan University.

    Returns:
        list: The bus location data as a list of dictionaries, or an error message string.
    """
    url = "http://route.hellobus.co.kr:8787/pub/routeView/skku/getSkkuLoc.aspx"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        bus_data = response.json()

        if not bus_data:
            return "Error: No bus data received."

        return bus_data # Return the raw data

    except requests.exceptions.RequestException as e:
        return f"Error: Could not fetch data from URL: {e}"
    except json.JSONDecodeError:
        return f"Error: Could not decode JSON response. Raw text: {response.text if 'response' in locals() else 'No response object'}"
    # Removed KeyError and general Exception as the primary goal is to return the data or a fetch/decode error.
    # The user can handle data structure issues themselves if they wish.

if __name__ == "__main__":
    result = get_latest_shuttle_bus_location()
    if isinstance(result, list): # Expecting a list of bus data now
        print("Shuttle Bus Location Data:")
        # ensure_ascii=False to correctly print Korean characters
        print(json.dumps(result, indent=4, ensure_ascii=False))
    else:
        print(result) # Print the error message
