// loadmonitor.ino /////////////////////////////////////////////////////////////
// Arduino-side code that recieves the info about what the current load ////////
// on the pi is via serial, then hopefully converts it to a number and dims ////
// a led based on that value ///////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////


// These constants won't change.  They're used to give names
// to the pins used:
const int analogOutPin = 9;
// Analog output pin that the LED is attached to
int incomingByte = 0;
// for incoming serial data
int outputValue = 255;
// value output to the PWM (analog out)
float loadValue = 100.0;
String inString = "";
// string to hold input

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600); 
}

void loop() {
	// send data only when you receive data:
	if (Serial.available() > 0)
	{
		
		// read the incoming byte:
		incomingByte = Serial.read();
		// say what you got:
		//Serial.println(incomingByte, DEC);
		//Serial.println(incomingByte, BIN);		

		//Serial.print("I received: ");
		//loadValue = Serial.parseFloat();
		if(char(incomingByte) == '\n')
		{	Serial.print("\n");
			Serial.print("Full string sent over serial is ");
			Serial.print(inString);
			loadValue = inString.toInt();
			
			outputValue = int(float(loadValue)*2.55);
			inString = "";
			Serial.print("Output at ");
			Serial.print(outputValue);
			Serial.print("%\n");
		}
		else
		{
			Serial.print(char(incomingByte));
			inString.concat(char(incomingByte));
		}

	}
	// map it to the range of the analog out:	
	// change the analog out value:
	analogWrite(analogOutPin, outputValue);           

	// wait 2 milliseconds before the next loop
	// for the analog-to-digital converter to settle
	// after the last reading:
	delay(2);                     
}


