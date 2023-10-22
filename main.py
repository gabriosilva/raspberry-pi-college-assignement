from app_lcd import AppLCD

app = AppLCD(sda_pin=4, scl_pin=5, num_rows=2, num_columns=16)
app.register_lcd()
app.display_message("Inteli Student")
