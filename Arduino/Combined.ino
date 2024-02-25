/*!
* @file HeartRateMonitor.ino
* @brief HeartRateMonitor.ino Sampling and ECG output
* 
* Real-time sampling and ECG output
*
* @author linfeng(490289303@qq.com)
* @version V1.0
* @date 2016-4-5
*/

#include <dht.h>

dht DHT;
#define DHT11_PIN 7

const int heartPin = A0;
const int senpin = A1;

void setup() {
  pinMode(senpin, INPUT);
  Serial.begin(115200);
  }

void loop() {
  int heartValue = analogRead(heartPin);
  Serial.print(heartValue);
  Serial.print(",");

  int val = analogRead(senpin);
  Serial.print(val);
  Serial.print(",");

  DHT.read11(DHT11_PIN);
  Serial.print(DHT.temperature);
  Serial.print(",");
  Serial.print(DHT.humidity);

  Serial.println();

  delay(50);
}

