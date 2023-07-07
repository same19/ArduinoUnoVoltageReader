void setup() {
  Serial.begin(9600);
}

void loop() {
  int r0 = analogRead(A0);
  int r1 = analogRead(A1);
  int r2 = analogRead(A2);
  int r3 = analogRead(A3);
  int r4 = analogRead(A4);
  int r5 = analogRead(A5);
  Serial.println((String)r0 + " " + (String)r1 + " " + (String)r2 + " " + (String)r3 + " " + (String)r4 + " " + (String)r5);
}
