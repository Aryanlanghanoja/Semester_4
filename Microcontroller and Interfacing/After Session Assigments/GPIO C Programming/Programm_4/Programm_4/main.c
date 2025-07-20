/*
 * Programm_4.c
 *
 * Created: 05-02-2024 19:19:54
 * Author : Aryan
 */ 

#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRB = 0xFF;
	PORTB = 0xFF;
	
	while (1)
	{
		PORTB = PORTB ^ 0x80 ;
		_delay_ms(10);
	}
	
	return 0;
}


