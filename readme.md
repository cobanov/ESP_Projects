## Flash 
### ESP32
`esptool.py --chip esp32 erase_flash`
`esptool.py --chip esp32 --port COM5 write_flash -z 0x1000 esp32-idf3-20191220-v1.12.bin`

### ESP8266
`esptool.py --port com5 write_flash -fm dio 0x00000 esp8266-20191220-v1.12.bin`
*Latest firmware is in the 'firmware' folder.*

## Ampy
List all files in the board
`ampy --port com5 ls`

Delete all files 
`ampy --port com5 rm boot.py`

Put files to board
`ampy --port com5 put boot.py`
`ampy --port com5 put main.py`

Then reset board and go to adress
http://192.168.1.24/

ESP32 Projesi
