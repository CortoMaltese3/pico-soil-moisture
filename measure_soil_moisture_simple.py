# import required modules
from machine import ADC, Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
 
# Assign soil moisture sensor PIN
soil_sensor = ADC(Pin(26))
 
# Calibrate min/max moisture values
min_moisture=39500
max_moisture=65535
 
read_delay = 1 											# delay between readings
 
WIDTH  = 128                                           	# oled display width
HEIGHT = 64                                           	# oled display height
 
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)     # Init I2C using pins GP0 & GP1 
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
 
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)               # Init oled display
 
while True:
    display.fill(0)
    # Read moisture value and convert to percentage into the calibration range
    moisture = (max_moisture - soil_sensor.read_u16()) * 100 / (max_moisture - min_moisture) 
    print("moisture: " + "%.2f" % moisture +"% (adc: "+str(soil_sensor.read_u16())+")")
    
    display.text("Soil moisture",10,0)
    display.text(str("%.2f" % moisture)+" %",35,32)
    display.show()
    
    utime.sleep(read_delay) # set a delay between readings  

