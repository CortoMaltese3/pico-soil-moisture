from machine import Pin, I2C
import ssd1306

i2c = I2C(0, sda=Pin(16), scl=Pin(17))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Hello', 0, 0)
display.text('world!', 0, 16)

display.show()
