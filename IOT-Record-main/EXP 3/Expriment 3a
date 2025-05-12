// Interfacing Motor with Arduino Via Relay and Control It with PushButton
#define PUSH_BUTTON 8 // Use push button with pull-down resistor.#define RELAY
7
bool motorState = false;void
setup()
{
pinMode(RELAY, OUTPUT);
pinMode(PUSH_BUTTON, INPUT);
}
void loop()
{
if(digitalRead(PUSH_BUTTON) == HIGH)
{
if(motorState == false) // If already OFF, turn it ON.
{
digitalWrite(RELAY, HIGH);
motorState = true;
}
else
{
digitalWrite(RELAY, LOW); // Else, turn it OFF.motorState =
false;
}
delay(100); // Delay to avoid debounce of push button.
}
}
