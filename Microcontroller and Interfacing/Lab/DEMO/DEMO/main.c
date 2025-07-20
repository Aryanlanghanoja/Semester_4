 /*
 * Experiment_2.c
 *
 * Created: 06-02-2024 13:43:44
 * Author : Aryan
 */ 

#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
			
    /* Replace with your application code */
	//int HexCodes[16] = {0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67,0x77,0x7C,0x39,0x5E,0x79,0x71};
	int HexCodes[16] = {0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x98,0x88,0x83,0xC6,0xA1,0x86,0x8E};
	DDRA = 0x00;
	PORTA = 0x03;
	DDRD = 0xFF;
	int i = 0 ;
	
    while (1) 
    {
		
		// Decimal Up
		while (PINA == 0x03) {
			if(i == 10) {
				i = 0 ;
			}
			
			PORTD = HexCodes[i] ;
			i++;
			_delay_ms(50);
		}
		
		// Decimal Down
		while (PINA == 0x02) {
			if(i == -1) {
				i = 9 ;
			}
			
			PORTD = HexCodes[i] ;
			i--;
			_delay_ms(50);
		}
		
		// Hex Up
		while (PINA == 0x01) {
			if(i == 16) {
				i = 0 ;
			}
			
			PORTD = HexCodes[i] ;
			i++;
			_delay_ms(50);
		}
		
		// Hex Down
		while (PINA == 0x00) {
			if(i == -1) {
				i = 15 ;
			}
			
			PORTD = HexCodes[i] ;
			i--;
			_delay_ms(50);
		}
		
    }
	
	return 0;
}

