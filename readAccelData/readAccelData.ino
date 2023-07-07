int amped = A0;
int diff = A1;
int singleEnded = A2;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int r0 = analogRead(amped);
  int r1 = analogRead(diff);
  int r2 = analogRead(singleEnded);
  Serial.println((String)r0 + " " + (String)r1 + " " + (String)r2);
}
