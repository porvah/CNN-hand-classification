// pwm levels
int pwm[] = {0, 65, 102, 153, 204, 255};
int indicator_bar[] = {2, 4, 6, 8, 10};

void setup() {
  // begining a serial connection
  Serial.begin(115200); 
  Serial.setTimeout(1); 
  // setting pin modes
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  // program stops until serial is available
  while (!Serial.available()); 

  // sets all LEDs to low
  for (int i = 0; i < 5; i++) {
    digitalWrite(indicator_bar[i], LOW);
  }

  
  // reads from serial
  int level = Serial.readStringUntil('\r').toInt();
  // applies pwm
  analogWrite(11, pwm[level]);
  // updates LED indicator
  for (int i = 0; i < level; i++) {
    digitalWrite(indicator_bar[i], HIGH);
  }


}
