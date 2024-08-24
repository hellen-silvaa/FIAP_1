int trigger = 7;
int echo = 8;
int dist = 0;

void setup(){
  pinMode(trigger, OUTPUT);
  pinMode(echo, INT);
  Seial.begin(9600);
}

void loop(){
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  dist = pulseIn(echo, HIGH);
  dist = dist / 58

  Serial.println("Distancia" + String(dist));
  delay(1000);
}
