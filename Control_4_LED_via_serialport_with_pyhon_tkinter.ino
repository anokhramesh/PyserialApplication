//Control 4 LEDes connected to Arduino pin # 8,9,10,11 via serial communication from python tkinter buttons.
char serialData;//created a variable name serialData char type
int led1 = 8;//created a variable name led1 int type and assigned as Arduino pin# 8
int led2 = 9;//created a variable name led2 int type and assigned as Arduino pin# 9
int led3 = 10;//created a variable name led3 int type and assigned as Arduino pin# 10
int led4 = 11;//created a variable name led4 int type and assigned as Arduino pin# 11
void setup()
{
pinMode (led1, OUTPUT);// initilized led1 as an output
pinMode (led2, OUTPUT);// initilized led2 as an output
pinMode (led3, OUTPUT);// initilized led3 as an output
pinMode (led4, OUTPUT);// initilized led4 as an output
  
  Serial.begin(9600);// serial comuunucation boud rate-9600
}
void loop()
{
  if (Serial.available() > 0)//check condition-serial data available
    serialData = Serial.read();
  Serial.print(serialData);
  if (serialData == 'a')// if serial data command is a
  {
    digitalWrite(led1, HIGH);// turn ON the led1
  }
  else if (serialData == 'b')// if serial data is b
  {
    digitalWrite(led1, LOW);// turn OFF the led1
  }
  if (serialData == 'c')// if serial data command is c
  {
    digitalWrite(led2, HIGH);// turn ON the led2
  }
  else if (serialData == 'd')// if serial data is d
  {
    digitalWrite(led2, LOW);// turn OFF the led2
  }
  if (serialData == 'e')// if serial data command is e
  {
    digitalWrite(led3, HIGH);// turn ON the led3
  }
  else if (serialData == 'f')// if serial data is f
  {
    digitalWrite(led3, LOW);// turn OFF the led3
  }
  if (serialData == 'g')// if serial data command is g
  {
    digitalWrite(led4, HIGH);// turn ON the led4
  }
  else if (serialData == 'h')// if serial data is h
  {
    digitalWrite(led4, LOW);// turn OFF the led4
  }
}
