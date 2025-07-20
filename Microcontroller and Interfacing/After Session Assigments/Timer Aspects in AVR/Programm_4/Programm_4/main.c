/*
 * Programm_4.c
 *
 * Created: 10-02-2024 20:59:09
 * Author : Aryan
 */ 

#include <avr/io.h>
#include <avr/delay.h>
#include <util/delay.h>
#define  F_CPU 16000000UL

void Generate_Delay() {
	TCNT0 = 0xF6 ;
	TCCR0 = 0x02 ;
	
	while(TCNT0 != 0) ;
}

int main(void)
{
	DDRB = 0xFF ;
	PORTB = 0x00 ;
	while (1) {
		PORTB = 0xFF ;
		Generate_Delay();
		PORTB ^= 0xFF ;
	}
}


