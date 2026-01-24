#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import *
from flight_search import *
import pandas

flight_sheet_info_manager = DataManager()
flight_search_logic = FlightSearch()

flight_sheet_info=flight_sheet_info_manager.get_flight_data()
updated_flight_sheet_info =flight_search_logic.get_iata_names(flight_sheet_info_manager)
flight_sheet_info_manager.update_flight_data(updated_flight_sheet_info)

# for entry in flight_sheet_info:
#     if entry['iataCode'] == '':
#         entry['iataCode']="TESTING"

# flight_sheet_info_manager.update_flight_data(flight_sheet_info)