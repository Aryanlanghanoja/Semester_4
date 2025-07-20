/*
 * Task_2.c
 *
 * Created: 08-02-2024 22:45:24
 * Author : Aryan
 */ 

#include <avr/io.h>
#include <util/delay.h>
#define F_CPU 16000000UL 

int main(void)
{
	DDRA = 0xFF ;
	DDRC = 0x00;
	DDRC = DDRC | 0x03 ;
	
    /* Replace with your application code */
    while (1) {
		if (PINC == 0x00) {
			PORTA = 0x00 ;
			_delay_ms(1000);
			PORTA = 0xFF ;
			_delay_ms(1000);
		}
		
		else if (PINC == 0x01) {
			PORTA = 0x01 ;
			_delay_ms(1000);
			
			while (PORTA != 0x80) {
				PORTA = PORTA << 1 ;
				_delay_ms(1000);
				
				if(PORTA == 0x80) {
					PORTA = 0x01 ;
					_delay_ms(1000) ;
				}
			}
		} 
		
		else if (PINC == 0x02) {
			PORTA = 0x80 ;
			_delay_ms(1000);
			
			while (PORTA != 0x01) {
				PORTA = PORTA >> 1 ;
				_delay_ms(1000);
				
				if(PORTA == 0x01) {
					PORTA = 0x80 ;
					_delay_ms(1000) ;
				}
			}
		}
		
		else if (PINC == 0x03) {
			
			while (1) {
				PORTA = 0xAA ;
				_delay_ms(1000) ;
				PORTA = 0x55 ;
				_delay_ms(1000) ;
			}
		}
		
    }
}

