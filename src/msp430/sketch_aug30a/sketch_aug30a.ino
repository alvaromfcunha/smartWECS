void setup()
{ 
  Serial.begin(9600);
}



void loop()
{
  char buffer[10];
  
  switch(Serial.read()){
    case 'e':
      delay(10);
      itoa(analogRead(A3),buffer,10);
      Serial.write(buffer);
      Serial.write("\n");
      break;
    case 'w':
      delay(10);
      itoa(analogRead(A4),buffer,10);
      Serial.write(buffer);
      Serial.write("\n");
      break;
  }
}
