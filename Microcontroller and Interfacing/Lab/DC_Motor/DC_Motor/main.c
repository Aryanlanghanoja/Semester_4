/*
 * DC_Motor.c
 *
 * Created: 19-3-2024 14:33:05
 * Author : Aryannn   
 */ 

#ifndef F_CPU
#define F_CPU 16000000UL // 16 MHz clock speed
#endif

#include <avr/io.h>        //standard AVR library
#include <util/delay.h>     // delay library

int main(void) //main starts
{
	DDRB= 0xFF; // direction of port B as output
	while(1)   //infinite loop
	{
		PORTB = 0x05; // motor rotation in clockwise direction
		_delay_ms(3000);    //delay of 3 sec
		
		PORTB = 0x00;// motor stopped
		_delay_ms(1000);    //delay of 1 sec
		
		PORTB = 0x0A; //motor rotation in anticlockwise direction
		_delay_ms(3000);    //delay of 3 sec
		
		PORTB = 0x00;// motor stopped
		_delay_ms(1000);    //delay of 1 sec
		
	}     //while loop end
}      //main end


