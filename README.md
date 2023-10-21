# script-sensor-from-tasmota
I needed to read data on Terrarium PI from an MLX90614 attached to an ESP32 flashed with Tasmota, and it wouldn't work normally as a remote sensor.

Now they are being used as script sensors.

These scripts will read that data and allow you to add the MLX90614 as a script sensor. There are 2 scripts, one for object temperature, and one for ambient temperature.
You will need to chmod them with a +x.
