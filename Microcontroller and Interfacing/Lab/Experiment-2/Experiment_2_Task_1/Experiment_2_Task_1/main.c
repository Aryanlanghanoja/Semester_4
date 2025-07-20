/*
 * Experiment_2_Task_1.c
 *
 * Created: 06-02-2024 21:54:55
 * Author : Aryan
 */ 

#include <avr/io.h>
#include <util/delay.h>
#define F_CPU 16000000UL;

void Pattern_0 () {
	PORTC = 0xFF;
	_delay_ms(500);
	PORTC = 0x00;
	_delay_ms(500);
}

void Pattern_1 () {
	PORTC = 0xAA;
	_delay_ms(500);
	PORTC = 0x55;
	_delay_ms(500);
}

void Pattern_2 () {
	PORTC = 0xF0;
	_delay_ms(500);
	PORTC = 0x0F;
	_delay_ms(500);
}

void Pattern_3 () {
	PORTC = 0x00;
	_delay_ms(500);
	PORTC = 0x01 ;
	
	while(PORTC != 0x00) {
		_delay_ms(500);
		PORTC = PORTC << 1 ;
		
		if(PORTC == 0xFF) {
			PORTC == 0x01 ;
		}
	}
}

void Pattern_4 () {
	PORTC = 0xFF ;
	_delay_ms(500);
	int Sequences[8] = {0xFE,0xFD,0xFB,0xF7,0xEF,0xDF,0xBF,0x7F};
		
		int i = 0 ;
		while (i <= 9) {
			PORTC = Sequences[i] ;
			_delay_ms(500);
			
			if(i == 9) {
				i = -1 ;
				PORTC = 0xFF;
				_delay_ms(500);
			}
			i++;
		}
}

void Pattern_5 () {
	PORTC = 0x00;
	_delay_ms(500);
	PORTC = 0x80 ;
	
	while(PORTC != 0x00) {
		_delay_ms(500);
		PORTC = PORTC >> 1 ;
		
		if(PORTC == 0x01) {
			PORTC == 0x80 ;
		}
	}	
}

void Pattern_6 () {
	PORTC = 0x00;
	_delay_ms(500);
	int Sequences[7] = {0x81,0x42,0x24,0x18,0x24,0x42,0x81};	
	
	int i = 0 ;
	while (i <= 7) {
		PORTC = Sequences[i] ;
		_delay_ms(500);
		i++;
		
		if(i == 8) {
			i = 0 ;
		}
	}
}

void Pattern_7 () {
	PORTC = 0x7F;	
}

void Pattern_8 () {
	PORTC = 0xFF;
}

void Pattern_9 () {
	PORTC = 0x00;
}

int main(void)
{
    /* Replace with your application code */
	DDRC = 0xFF;
	DDRB = 0x00;
	DDRB = DDRB | 0xF0 ;
	
    while (1) {
		
		if(PINB == 0x00) {
			Pattern_0();
		}
		
		if (PINB == 0x01) {
			Pattern_1();
		}
		
		if (PINB == 0x02) {
			Pattern_2();
		}
		
		if (PINB == 0x03) {
			Pattern_3();
		}
		
		if (PINB == 0x04) {
			Pattern_4();
		}
		
		if (PINB == 0x05) {
			Pattern_5();
		}
		
		if (PINB == 0x06) {
			Pattern_6();
		}
		
		if (PINB == 0x07) {
			Pattern_7();
		}
		
		if (PINB == 0x08) {
			Pattern_8();
		}
		
		if (PINB == 0x09) {
			Pattern_9();
		}
    }
}

