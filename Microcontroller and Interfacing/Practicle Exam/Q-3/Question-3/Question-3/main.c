/*
 * Question-3.c
 *
 * Created: 12-04-2024 14:09:40
 * Author : Aryan
 */ 

#include <avr/io.h>
#include <util/delay.h>
#include <avr/delay.h>
#define F_CPU 16000000UL

int main(void)
{
    DDRB = 0xFF;
	for(int i = 0 ; i< 5 ; i++) {
		PORTB = 0xFF;
		_delay_ms(1000);
		PORTB = 0x00;
		_delay_ms(1000);
	}
		
	for(int i = 0 ;i < 5 ; i++) {
		PORTB = 0xF0 ;
		_delay_ms(1000);
		PORTB = 0x0F;
		_delay_ms(1000);	
	}
		
	for(int i = 0 ; i < 5 ; i++) {
		PORTB = 0xCC ;
		_delay_ms(1000);
		PORTB = 0x33;
		_delay_ms(1000);
	}
		
	for(int i = 0 ; i < 5 ; i++) {
		PORTB = 0xAA ;
		_delay_ms(1000);
		PORTB = 0x55;
		_delay_ms(1000);
	}
		
	PORTB = 0x80;
	for(int i = 0 ; i < 8 ; i++) {
		PORTB = 1<<i;
		_delay_ms(1000);	
	}
	
	while(1);
	
	return 0;
}

