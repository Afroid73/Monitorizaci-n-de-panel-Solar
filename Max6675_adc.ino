#include "max6675.h"
float lectura, lectura2;
float volt,volt2;
float temp = 0;
//-------------------------------//
#define CONFIG_TCGND_PIN      8
#define CONFIG_TCVCC_PIN      9
#define CONFIG_TCSCK_PIN      10
#define CONFIG_TCCS_PIN       11
#define CONFIG_TCDO_PIN       12
//------------------------------//
MAX6675 thermocouple(CONFIG_TCSCK_PIN, CONFIG_TCCS_PIN, CONFIG_TCDO_PIN);
//------------------------------//

void setup() {
  Serial.begin(9600);
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
  pinMode(CONFIG_TCVCC_PIN, OUTPUT); digitalWrite(CONFIG_TCVCC_PIN, HIGH);
  pinMode(CONFIG_TCGND_PIN, OUTPUT); digitalWrite(CONFIG_TCGND_PIN, LOW);
  delay(500);
}
void loop() {
  lectura = analogRead(A0);
  volt = lectura /1023 * 5.0;

  lectura2 = analogRead(A1);
  volt2 = lectura2 /1023 * 5.0;

  temp = float(thermocouple.readCelsius());

  Serial.print(volt);
  Serial.print(",");
  Serial.print(volt2);
  Serial.print(",");
  Serial.println(temp);
  
  delay(1000);
}
