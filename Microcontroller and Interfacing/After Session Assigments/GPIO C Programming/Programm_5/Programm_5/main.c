/*
 * Programm_5.c
 *
 * Created: 05-02-2024 19:19:54
 * Author : Aryan
 */ 

#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRC = 0x00;
	DDRB = 0xFF;
	
	
	while (1)
	{
		if(PINC ==  0x20) {
			PORTB = 0xFF ;
		}
		
		else {
			PORTB = 0x00 ;
		}
	}
	
	return 0;
}


