// === Harrison Olvera ====
// Final Project Component – Option 2

#include <Wire.h>  //lcd
#include <LiquidCrystal_I2C.h> //lcd
LiquidCrystal_I2C lcd(0x3F,16,2); //set the LCD address to 0x27 for a 16 chars and 2-line display
// if it does not work then try 0x3F, if both addresses do not work then run the scan code below
const int bzr=32;      // GPIO32 to connect the Buzzer

// Set GPIOs for LED and PIR Motion Sensor
const int led = 16; // Flashing White (Blue) Led
const int motionSensor = 17;
int pirState = 0 ;
int j,Em_value,Xw_value;

const int Em_button = 23;  // Emergency button
const int Xw_button = 19; //Cross Walk button

//==================== LCD ====================
const int red_LED1  = 14;   // The red LED1 is wired to ESP32 board pin GPIO04
const int yellow_LED1  =12;   // The yellow LED1 is wired to ESP32 board pin GPIO12
const int green_LED1 = 13; // The green LED1 is wired to ESP32 board pin GPIO13
const int red_LED2  = 25;   // The red LED2 is wired to Mega board pin GPIO25
const int yellow_LED2  = 26;   // The yellow LED2 is wired to Mega board pin GPIO 26
const int green_LED2 = 27; // The green LED2 is wired to Mega board pin GPIO 27
 
void setup() {
//================Motion Detector initialization =====
  // PIR Motion Sensor mode INPUT
  pinMode(motionSensor, INPUT);
  pinMode(Em_button, INPUT_PULLUP);  // 0=pressed, 1 = unpressed button
  pinMode(Xw_button, INPUT_PULLUP); // 0=pressed, 1 = unpressed button
  pinMode(bzr,OUTPUT);
  pinMode(led, OUTPUT); 
  digitalWrite(led, LOW);  // Set Flashing White (Blue) Light to LOW

//=======================================
  Serial.begin(115200);
lcd.init(); // initialize the lcd
lcd.backlight();
lcd.setCursor(0,0); // column#1 and Row #1
lcd.print(" === CEIS114 ===");// can be replaced with your name
  
  
 pinMode(red_LED1, OUTPUT);  // initialize digital pin 14 (Red LED1) as an output.
 pinMode(yellow_LED1, OUTPUT);  // initialize digital pin 12 (yellow LED1) as an output.
 pinMode(green_LED1, OUTPUT);    // initialize digital pin 13 (green LED1) as an output.

 pinMode(red_LED2, OUTPUT);  // initialize digital pin 25(Red LED2) as an output.
 pinMode(yellow_LED2, OUTPUT); // initialize digital pin 26 (yellow LED2) as an output.
 pinMode(green_LED2, OUTPUT); // initialize digital pin 27 (green LED2) as an output.
}

// the loop function runs over and over again forever
void loop() {

// Check the emergency button
int  Em_value=digitalRead(Em_button);
 if (Em_value == 0){ // Emergency button was pressed so allow about 10 seconds 
skipnow: // jump here in case of emergency ====================
Serial.println("Emergency button was pressed ");
// Both sides are RED with flashing White (Blue) light
  digitalWrite(yellow_LED1 , LOW);        //  This should turn off the YELLOW LED1
  digitalWrite(green_LED1, LOW);        //  This should turn off the GREEN LED1
  digitalWrite(red_LED1, HIGH);      // This should turn on the RED LED1

  digitalWrite(red_LED2, HIGH);         // This should turn on the RED LED2
  digitalWrite(yellow_LED2 , LOW);  //  This should turn off the YELLOW LED2
  digitalWrite(green_LED2, LOW);   //  This should turn off the GREEN LED2

   for (j=0;j<10;j++){ // total of 10 seconds, can be changed
     digitalWrite(led,HIGH);
     delay(500); //Flashing white (blue) light every .5 sec -- ON
    digitalWrite(led,LOW);
    delay(500); //Flashing white (blue) light every .5 sec -- OFF
  }
} // End of (if) statement for Emergency button

  Em_value=digitalRead(Em_button);
  int Xw_value=digitalRead(Xw_button);
   pirState = digitalRead(motionSensor);

 if (Em_value == 1){ // Emergency button not pressed 

 if (pirState == 1 || Xw_value == 0 ){ // Emergency button not pressed, X-button or motion pressed 
// Transition: If a button is pressed, yellow on major street for 1sec. before switching  
  if(pirState == 1){Serial.println("motion detected");}

    delay(500);
   digitalWrite(green_LED1, LOW);   //  This should turn off the GREEN LED1
  digitalWrite(yellow_LED1, HIGH);      // This should turn on the Yellow LED1
delay(1500);
  digitalWrite(bzr, HIGH);
  digitalWrite(yellow_LED1 , LOW);        //  This should turn off the YELLOW LED1
  digitalWrite(green_LED1, LOW);        //  This should turn off the GREEN LED1
  digitalWrite(red_LED1, HIGH);      // This should turn on the RED LED1
  digitalWrite(red_LED2, LOW);         // This should turn off the RED LED2
  digitalWrite(yellow_LED2 , LOW);  //  This should turn off the YELLOW LED2
  digitalWrite(green_LED2, HIGH);   //  This should turn on the GREEN LED2

// LED1 is a major street
for (int i=10; i>= 0; i--) {
    Em_value=digitalRead(Em_button);// check for emergency button pressing
     if (Em_value == 0)goto skipnow;  // if so break and execute emergency at skipnow label 
    
  Serial.print(" Count =  ");
  Serial.print(i);
  Serial.println("  == Walk ==  ");
   lcd.setCursor(0,1); // set the cursor to column 1, line 2
// lcd.clear();   // clears the display to print new message
   lcd.print("                ");
   lcd.setCursor(0,1); // set the cursor to column 1, line 2
   lcd.print(" == Walk ==   "); // display Walk characters to the LCD.
   lcd.print(i); // Display the count 
  delay(1000); 
  digitalWrite(bzr, LOW);
delay(500); 
 } // End of counter  
 // clears the display to print new message
 // ===== lcd.clear();
    lcd.setCursor(0,1); // set the cursor to column 1, line 2
   lcd.print("                ");
 
//====================================
// Transition
 digitalWrite(green_LED2 , LOW);  //  This should turn off the YELLOW LED2
 digitalWrite(yellow_LED2 , HIGH);  //  This should turn off the YELLOW LED2
delay(1000);
 } // End of  Emergency button not pressed, X-button pressed or Motion was detected
} //End of  Emergency button not pressed
 
//===============================================
 
// No motion, No Emergency, No crossing, then LED1=Green, LED2=Red always
 lcd.setCursor(0,1); // set the cursor to column 1, line 2
  lcd.print(" = Do Not Walk ="); // Display Do Not Walk characters to the LCD. 
    
  Serial.println("  == Do Not Walk ==  ");

  digitalWrite(yellow_LED1 , LOW);        //  This should turn off the YELLOW LED1
  digitalWrite(green_LED1, HIGH);        //  This should turn on the GREEN LED1
  digitalWrite(red_LED1, LOW);      // This should turn off the RED LED1

  digitalWrite(red_LED2, HIGH);         // This should turn on the RED LED2
  digitalWrite(yellow_LED2 , LOW);  //  This should turn off the YELLOW LED2
  digitalWrite(green_LED2, LOW);   //  This should turn off the GREEN LED2
  
 delay(1000);

//====================End Motion ==========  
}// End of loop
