
int tp1 = A0;
int tp2 = A1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int tv1 = analogRead(tp1);
  int tv2 = analogRead(tp2);

  float vv1 = tv1 * (5.0/1023.0);
  float vv2 = tv2 * (5.0/1023.0);

  Serial.println(vv1);
  Serial.println(vv2);
  delay(500);
}