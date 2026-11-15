
import time
import board
import adafruit_dht

# DHT11 DATA 接 GPIO17（實體 Pin 11）
dht = adafruit_dht.DHT11(board.D17)

print("Student ID: N97141483")
print("Lab4-1 DHT11 Temperature and Humidity")
print("Press Ctrl+C to stop")

try:
    while True:
        try:
            celsius = dht.temperature
            humidity = dht.humidity

            if celsius is not None and humidity is not None:
                fahrenheit = celsius * 9 / 5 + 32

                print(
                    f"Temperature: {celsius:.1f} C / "
                    f"{fahrenheit:.1f} F | "
                    f"Humidity: {humidity:.1f} %"
                )

        except RuntimeError as error:
            print(f"Reading failed: {error}")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nProgram stopped")

finally:
    dht.exit()
