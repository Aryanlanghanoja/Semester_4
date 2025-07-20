/*
 * Programm_5.c
 *
 * Created: 10-02-2024 21:05:01
 * Author : Aryan
 */ 

#include <avr/io.h>
#include <avr/delay.h>
#include <util/delay.h>
#define  F_CPU 16000000UL

void Generate_Delay() {
	TCNT0 = 0xBB ;
	TCCR0 = 0x02 ;
	
	while(TCNT0 != 0) ;
}

int main(void)
{
	DDRB = 0xFF ;
	PORTB = 0x00 ;
	while (1) {
		PORTB = 0x10 ;
		Generate_Delay();
		PORTB ^= 0x10 ;
	}
}


