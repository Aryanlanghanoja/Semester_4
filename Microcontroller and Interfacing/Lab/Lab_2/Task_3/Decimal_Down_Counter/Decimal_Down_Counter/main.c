/*
 * Decimal_Down_Counter.c
 *
 * Created: 08-02-2024 23:33:51
 * Author : Aryan
 */ 

#include <avr/io.h>
#include <avr/delay.h>
#include <util/delay.h>
#define F_CPU 16000000UL 

int main(void)
{
    /* Replace with your application code */
	int HexCodes[10] = {0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x98};
	
	
	DDRA = 0xFF;
	int i = 9 ;
	
    while (i >= 0) {
		PORTA = HexCodes[i] ;
		_delay_ms(1000) ;
		i--;
		
		if(i == -1) {
			i = 9 ;
		}
    }
}

