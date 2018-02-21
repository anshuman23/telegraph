# Telegraph (Work in progress)
###### An IoT device network simulator
# Dependencies
- pip install runp
- For mac users install Xquartz software

# How to run

- Simply type ```python main.py <number of the type of devices in the room(max 7)> <1st_device_name> <1st_device_quantity> <2nd_device_name> <2nd_device_quantity>...so on``` to run the simulator for a one room
- Devices are currently only of 7 types - ```smart_motion_detector_camera```, ```smart_temperature_sensor```, ```smart_lock```, ```smart_lights```, ```smart_toaster```, ```smoke_detector``` and ```smart_ac```
- An example of running simulation of one room with 1 smart_motion_detector_camera and 1 smart_temperature_sensor is```python main.py 2 smart_motion_detector_camera 1 smart_temperature_sensor 1```
- To quit the simulation simple kill the process by pressing ```Ctrl + C```

# Notes

- The data is stored in the data sub directory and are csv timeseries data with unix timestamp values and 
  - temperature in degree celsius for ```smart_temperature_sensor```
  - length of data file for ```smart_motion_detector_camera```. The actual simulated and appended camera feed (mpeg2) is stored as a separate mpeg2
