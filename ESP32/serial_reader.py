import serial
import pyautogui as pag

SERIAL_PORT = 'COM5'
SERIAL_RATE = 115200

def main():
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    threshold = 0.5
    while True:
        reading = float(ser.readline().decode('utf-8')) / 100
        value = round(reading - threshold)
        threshold = reading
        if value > 0:
            pag.press("left", abs(value))
        elif value < 0:
            pag.press("right", abs(value))
        else:
            pass

        print(f"Reading : {reading}, Threshold: {threshold}, Value: {value}")
        

if __name__ == "__main__":
    main()