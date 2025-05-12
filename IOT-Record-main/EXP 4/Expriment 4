#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
#include <SoftwareSerial.h>

#define DHTPIN 4
#define DHTTYPE DHT11

SoftwareSerial BTSerial(2, 3); // RX, TX
DHT_Unified dht(DHTPIN, DHTTYPE);

void setup() {
  BTSerial.begin(9600);
  dht.begin();
}

void loop() {
  if (BTSerial.available()) {
    sensors_event_t event;
    dht.temperature().getEvent(&event);
    if (!isnan(event.temperature)) {
      BTSerial.print("Temperature: ");
      BTSerial.print(event.temperature);
      BTSerial.println(" *C");
    }
    dht.humidity().getEvent(&event);
    if (!isnan(event.relative_humidity)) {
      BTSerial.print("Humidity: ");
      BTSerial.print(event.relative_humidity);
      BTSerial.println(" %");
    }
    delay(1000);
  }
}
