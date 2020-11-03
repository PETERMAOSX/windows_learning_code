import processing.serial.*;
import Leap.voidplus.*;

Serial port;
LeapMotion leap;

void setup()
{port = new Serial(this,"COM9",9600);
	leap = new leapMotion(this);
}
void draw()
{
	int fps; = leap.getFrameRate();
	for(Hand hand : leap.getHands)
	{
		boolean handIsLeft = hand.isLeft();
		boolean handIsRight = hand.isRight();
		if(handIsLeft)
		{
			port.write("a");
			println("Lefthand");
		}
		else if(handIsRight)
		{
			port.write("b");
			println("RIghthand")；
		}
	}
	
}