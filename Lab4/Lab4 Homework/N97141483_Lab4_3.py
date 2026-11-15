
import serial
import time
import tm1637

# UART 設定（助教 PPT）
ser = serial.Serial(
    port='/dev/serial0',
    baudrate=9600,
    timeout=1
)

# TM1637 七段顯示器設定
# CLK 接 GPIO18，DIO 接 GPIO27
display = tm1637.TM1637(clk=18, dio=27)
display.brightness(3)


# UART 傳送資料
def send_data(data):
    if ser.is_open:
        ser.write(data.encode('utf-8'))
        print(f"已傳送：{data.strip()}")


# UART 接收資料
def receive_data():
    if ser.is_open:
        incoming = ser.readline().decode(
            'utf-8', errors='ignore'
        ).strip()

        if incoming:
            print(f"收到資料：{incoming}")

        return incoming

    return ""


# 主程式
try:
    number = 0

    while True:
        # 傳送數字
        send_data(f"{number}\n")

        time.sleep(0.2)

        # 接收數字
        received = receive_data()

        # 顯示在七段顯示器
        if received.isdigit():
            display.number(int(received))
            print(f"LED 顯示：{received}")

        number = (number + 1) % 10
        time.sleep(1)

except KeyboardInterrupt:
    print("程式中斷")

finally:
    display.write([0, 0, 0, 0])
    if ser.is_open:
        ser.close()
        print("串列埠已關閉")
    