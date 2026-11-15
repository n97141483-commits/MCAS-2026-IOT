
import RPi.GPIO as GPIO
import time

# 設定使用 BCM 編號系統
GPIO.setmode(GPIO.BCM)

# 超音波模組的 TRIG 與 ECHO 引腳設定
TRIG_y = 23  # GPIO23，實體 Pin 16
ECHO_r = 24  # GPIO24，實體 Pin 18

# 設定引腳輸出入模式
GPIO.setup(TRIG_y, GPIO.OUT)
GPIO.setup(ECHO_r, GPIO.IN)


def measure_distance():
    # 確保發射端是關閉的，並稍作延遲讓感測器穩定
    GPIO.output(TRIG_y, False)
    time.sleep(0.5)

    # 發送 10 微秒的高電位脈衝來觸發超聲波
    GPIO.output(TRIG_y, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_y, False)

    # 等待 ECHO 變高電位，並記錄起始時間
    timeout = time.monotonic() + 0.05
    while GPIO.input(ECHO_r) == 0:
        if time.monotonic() > timeout:
            raise RuntimeError("等待 ECHO 高電位逾時")
    pulse_start = time.monotonic()

    # 等待 ECHO 變回低電位，並記錄結束時間
    timeout = time.monotonic() + 0.05
    while GPIO.input(ECHO_r) == 1:
        if time.monotonic() > timeout:
            raise RuntimeError("等待 ECHO 低電位逾時")
    pulse_end = time.monotonic()

    # 計算脈衝持續時間，換算成距離（公分）
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance


try:
    print("Student ID: N97141483")
    print("Lab4-2 HC-SR04 Distance Measurement")
    print("程式啟動，按 Ctrl+C 可以停止測試...")

    while True:
        try:
            distance = measure_distance()

            # LAB4-2：判斷距離並輸出訊息
            print(f"目前距離：{distance:.2f} cm")

            if distance < 20:
                print("注意！！！")
            else:
                print("沒事")

        except RuntimeError as err:
            print(f"測距失敗：{err}")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n停止測量中...")

finally:
    GPIO.cleanup()
    print("GPIO 已清理，程式結束。")
