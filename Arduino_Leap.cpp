int c;

void setup()
{
	Serial.begin(9600);
}

void loop()
{
	if(Serial.available())
	{
		if(c == 97)
		{
			//97 = 'a'
		}
		else if(c == 98)
		{
			// 98 = 'b'
		}
	}
	
}