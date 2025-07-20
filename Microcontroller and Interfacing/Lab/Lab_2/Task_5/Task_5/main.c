/*
 * Task_5.c
 *
 * Created: 09-02-2024 00:23:58
 * Author : Aryan
 */ 

#include <avr/io.h>
#include <avr/delay.h>
#include <util/delay.h>
#define F_CPU 16000000UL 

int main(void)
{

    /* Replace with your application code */
	DDRA = 0xFF ;
	DDRC = 0xFF ;
	
	int HexCodes[10] = {0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x98};
		
    while (1) {
		PORTA = 0x00 ;
		PORTC = 0x00 ;
		
		int i = 0 ;
		int j = 0 ;
		
		while(i <= 9) {
			j = 0 ;
			while(j <= 9) {
				PORTA = HexCodes[i];
				PORTC = HexCodes[j];
				_delay_ms(500);
				j++;
			}
			i++ ;
			
			if(i == 10) {
				i = 0 ;
			}
		}
		
    }
}

