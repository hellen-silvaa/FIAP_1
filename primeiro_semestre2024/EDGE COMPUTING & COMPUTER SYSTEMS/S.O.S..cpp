int led = 13;
void setup()
{
  pinMode(13, OUTPUT); //LED 
}

void loop()
{
  
  //S
  for(int x = 0;  x< 3; x++){
  
    digitalWrite (13, HIGH);
    delay (1000);
    digitalWrite (13, LOW);
    delay (1000);
  }
  
  //O
   for(int x = 0;  x< 3; x++){
    digitalWrite (13, HIGH);
    delay (2000);
    digitalWrite (13, LOW);
    delay (1000);
  }
  
    //S
  for(int x = 0;  x< 3; x++){
  
    digitalWrite (13, HIGH);
    delay (1000);
    digitalWrite (13, LOW);
    delay (1000);
  }
}
