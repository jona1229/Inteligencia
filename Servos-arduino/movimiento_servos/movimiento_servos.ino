#include <Servo.h>

Servo px;
Servo py;
int p_y = 90;
int p_x = 90;
int lectura = 0;
void setup() {
  Serial.begin(9600);
  py.attach(9);
  px.attach(6);
  py.write(p_y);
  px.write(p_x);

}

void loop() {
  if (Serial.available() >= 1) {
    lectura = Serial.read();
  }
  if (lectura == 'D')
  {
    p_y = p_y + 1;
    py.write(p_y);
    delay(200);
  }
  if (lectura == 'U')
  {
    p_y = p_y - 1;
    py.write(p_y);
    delay(200);
  }
  if (lectura == 'L')
  {
    p_x = p_x + 1;
    px.write(p_x);
    delay(200);
  }
  if (lectura == 'R')
  {
    p_x = p_x - 1;
    px.write(p_x);
    delay(200);
  }

}
