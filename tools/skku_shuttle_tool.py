import requests
import json
from datetime import datetime # Keep datetime for potential future use or consistency
from pydantic import BaseModel, Field

# Import the function from shuttlebus.py
from tools.shuttlebus import get_latest_shuttle_bus_location

class Tools:
    def __init__(self):
        pass

    def get_skku_shuttle_bus_info(self) -> list | str:
        """
        Fetches the latest shuttle bus location data for Sungkyunkwan University.
        Returns the raw bus location data as a list of dictionaries, or an error message string.
        """
        return get_latest_shuttle_bus_location()

    # You can add other tools here if needed, following the example_tool.py structure.
    # For example:
    # def get_current_time(self) -> str:
    #     """
    #     Get the current time in a more human-readable format.
    #     """
    #     now = datetime.now()
    #     current_time = now.strftime("%I:%M:%S %p")
    #     current_date = now.strftime("%A, %B %d, %Y")
    #     return f"Current Date and Time = {current_date}, {current_time}"

# Example of how to test this tool (optional)
if __name__ == "__main__":
    tool_instance = Tools()
    bus_info = tool_instance.get_skku_shuttle_bus_info()
    if isinstance(bus_info, list):
        print("SKKU Shuttle Bus Info:")
        print(json.dumps(bus_info, indent=4, ensure_ascii=False))
    else:
        print(bus_info) # Print error message
