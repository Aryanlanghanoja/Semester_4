#include <avr/io.h>

int main(void)
{
    
	DDRB = 0xFF;
	DDRC = 0x00;
	PORTC = 0xFF;
	
    while (1) 
    {
		unsigned char input = PINC;
		PORTB = PINC ;
    }
}

