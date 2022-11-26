{
  "version": 1,
  "author": "Uri Shaked",
  "editor": "wokwi",
  "parts": [
    { "type": "wokwi-esp32-devkit-v1", "id": "esp", "top": 0, "left": 0, "attrs": {} },
    { "type": "wokwi-dht22", "id": "dht1", "top": -2.2, "left": 176.84, "attrs": {} }
  ],
  "connections": [
    [ "esp:TX0", "$serialMonitor:RX", "", [] ],
    [ "esp:RX0", "$serialMonitor:TX", "", [] ],
    [ "esp:3V3", "dht1:VCC", "red", [ "v3.65", "h88.37" ] ],
    [ "esp:GND.1", "dht1:GND", "black", [ "h105.7", "v-12.18", "h15.33" ] ],
    [ "esp:D4", "dht1:SDA", "green", [ "h76.37", "v-20.52", "h22.67" ] ]
  ]
}