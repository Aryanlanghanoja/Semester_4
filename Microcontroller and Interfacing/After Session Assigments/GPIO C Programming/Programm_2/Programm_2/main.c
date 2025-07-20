/*
 * Programm_2.c
 *
 * Created: 05-02-2024 19:19:54
 * Author : Aryan
 */ 

#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRB = 0x00;
	DDRC = 0xFF;
	
	while (1)
	{
		PORTC = PINB ;
	}
	
	return 0;
}


