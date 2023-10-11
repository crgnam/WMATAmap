# WMATA Map Visualizer
This longterm goal of this project is to produce a RaspberryPi powered wall map with addressable LEDs attached to the back of a WMATA system map.

Currently, just to get practice with [WMATA's API](https://developer.wmata.com/), it is simply displaying the data in real-world coordinates.  The mapping of the CircuitIDs to Lat/Long coordinates is included in `data/track-circuit-gps-coords.json` and was provided by the developers of the now sunset [MetroHero](https://github.com/jamespizzurro/metrohero-server).

## Running
To run any of this code you'll first need to obtain an API Key with WMATA.  Once that is done, simply copy the primary key to a file named `primary_api_key` and save it to the root directory of this repository (this file will not be tracked by git).

- `api_demo.py`: This script simply fetches the current train positions, and the standard routes.  IT will dump this data into `output_positions.json` and `output_standard_routes.json`.
- `continuous_log.py`: This will create a new subdirectory called `logging` and will periodically query the WMATA API, putting the time-stamped response in json format into the logging directory.  (The default is one query every 30 seconds, for 3 hours).