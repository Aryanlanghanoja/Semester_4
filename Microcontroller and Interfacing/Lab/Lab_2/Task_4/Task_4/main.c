/*
 * Task_4.c
 *
 * Created: 08-02-2024 21:49:24
 * Author : Aryan
 */ 

#include <avr/io.h>
#include <avr/delay.h>
#include <util/delay.h>
#define F_CPU 16000000UL


int main(void)
{
	
	/* Replace with your application code */
	int HexCodes[16] = {0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x98,0x88,0x83,0xC6,0xA1,0x86,0x8E};
	DDRA = 0x00;
	//PORTA = 0x03;
	DDRD = 0xFF;
	int i = 0 ;
	
	while (1)
	{
		// Decimal Up
		while (PINA == 0x00) {
			if(i == 10) {
				i = 0 ;
			}
			
			PORTD = HexCodes[i] ;
			i++;
			_delay_ms(500);
		}
		
		// Decimal Down
		while (PINA == 0x01) {
			if(i == -1) {
				i = 9 ;
			}
			
			PORTD = HexCodes[i] ;
			i--;
			_delay_ms(500);
		}
		
		// Hex Up
		while (PINA == 0x02) {
			if(i == 16) {
				i = 0 ;
			}
			
			PORTD = HexCodes[i] ;
			i++;
			_delay_ms(500);
		}
		
		// Hex Down
		while (PINA == 0x03) {
			if(i == -1) {
				i = 15 ;
			}
			
			PORTD = HexCodes[i] ;
			i--;
			_delay_ms(500);
		}
		
	}
	
	return 0;
}





