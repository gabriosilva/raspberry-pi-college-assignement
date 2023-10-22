# Author: Gabrio Lina

import machine
from i2c_lcd import I2cLcd

class AppLCD:
    def __init__(self, sda_pin, scl_pin, num_rows, num_columns):
        """Initialize the AppLCD with pin details and dimensions."""
        self.sda_pin = machine.Pin(sda_pin)
        self.scl_pin = machine.Pin(scl_pin)
        self.num_columns = num_columns
        self.num_rows = num_rows
        self.i2c = None
        self.lcd = None

    def _init_i2c(self):
        """Initialize the I2C bus."""
        if self.i2c is None:
            self.i2c = machine.I2C(id=0, sda=self.sda_pin, scl=self.scl_pin, freq=10000)
        return self.i2c

    def _search_i2c_device(self):
        """Search and return the I2C address of the LCD."""
        devices = self.i2c.scan()
        if not devices:
            raise Exception("No I2C device was found.")
        else:
            print("{0} I2C Devices found:".format(len(devices)))
            for device in devices:
                print("Device found at", hex(device))
            return devices[0]

    def register_lcd(self):
        """Initialize the I2C bus and register the LCD."""
        self._init_i2c()
        if self.lcd is None:
            lcd_addr = self._search_i2c_device()
            self.lcd = I2cLcd(self.i2c, lcd_addr, self.num_rows, self.num_columns)
            print("LCD Registered with success!")
    
    def display_message(self, message):
        """Display the provided message on the LCD."""
        if self.i2c is None or self.lcd is None:
            self.register_lcd()
        self.lcd.putstr(message)

    def clear_display(self):
        """Clear the LCD display."""
        if self.lcd:
            self.lcd.clear()

    def set_cursor(self, col, row):
        """Set the cursor position on the LCD."""
        if self.lcd:
            self.lcd.move_to(col, row)