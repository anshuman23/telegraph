# Telegraph (Work in progress)
###### An IoT device network simulator


# How to run

- Simply type ```python run.py <device_name> <ip> <port> <id>``` to run the simulator for a particular device
- Devices are currently only of two types - ```smart_motion_detector_camera``` and ```smart_temperature_sensor```
- An example of running smart camera with id-1 on localhost at port 8000 would be ```python run.py smart_motion_detector_camera 127.0.0.1 8000 1```
- To quit the simulation simple kill the process by pressing ```Ctrl + C```

# Notes

- The data is stored in the data sub directory and are csv timeseries data with unix timestamp values and 
  - temperature in degree celsius for ```smart_temperature_sensor```
  - length of data file for ```smart_motion_detector_camera```. The actual simulated and appended camera feed (mpeg2) is stored as a separate mpeg2
