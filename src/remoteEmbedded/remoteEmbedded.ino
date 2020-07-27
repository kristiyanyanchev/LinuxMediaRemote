#include "IRremote.h"
#include <ir_Lego_PF_BitStreamEncoder.h>

#define IRpin_PIN      PIND
#define IRpin          2

unsigned int Signal_0_0[] = {};
int khz=38;
decode_results results;
IRrecv irrecv(IRpin);

void setup(void) {
  
  irrecv.enableIRIn();
  Serial.begin(9600);
  Serial.println("Ready to decode IR!");
}
 
void loop(void) {
   if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    irrecv.resume(); // Continue receiving
  }

}
 
