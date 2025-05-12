// interfacing dht11 with arduino to print temeperature and humidity
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT_Unified dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  sensors_event_t event;
  dht.temperature().getEvent(&event);
  if (!isnan(event.temperature)) {
    Serial.print("Temperature: ");
    Serial.print(event.temperature);
    Serial.println(" *C");
  }
  dht.humidity().getEvent(&event);
  if (!isnan(event.relative_humidity)) {
    Serial.print("Humidity: ");
    Serial.print(event.relative_humidity);
    Serial.println(" %");
  }
  delay(1000);
}
