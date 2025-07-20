/*
 * Programm_3.c
 *
 * Created: 10-02-2024 12:52:02
 * Author: Aryan
 */ 

#include <avr/io.h>
#include <avr/delay.h>
#include <util/delay.h>
#define  F_CPU 16000000UL

void Generate_Delay() {
	TCNT0 = 0xCE ;
	TCCR0 = 0x01 ;
	
	while (TCNT0 != 0) ;
}

int main(void)
{
	PORTB = 0x00 ;
	while (1) {
		PORTB = 0x08 ;
		Generate_Delay();
		PORTB ^= 0x08 ;
	}
}



