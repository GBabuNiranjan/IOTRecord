const int buzzerPin = 8;

bool buzzerEnabled = false;
unsigned long previousMillis = 0;
bool buzzerState = false;
const long interval = 1000;  // 1 second

void setup() {
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Check for new serial input
  if (Serial.available()) {
    char command = Serial.read();
    if (command == '1') {
      buzzerEnabled = true;  // Enable blinking buzzer
    } else {
      buzzerEnabled = false;  // Disable buzzer completely
      digitalWrite(buzzerPin, LOW);  // Ensure it's off
    }
  }

  // Toggle buzzer if enabled
  if (buzzerEnabled) {
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;
      buzzerState = !buzzerState;
      digitalWrite(buzzerPin, buzzerState ? HIGH : LOW);
    }
  }
}