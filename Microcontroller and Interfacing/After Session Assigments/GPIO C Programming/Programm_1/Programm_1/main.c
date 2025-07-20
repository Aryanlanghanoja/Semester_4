/*
 * Programm_1.c
 *
 * Created: 05-02-2024 18:34:12
 * Author : Aryan
 */ 

#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    DDRB = 0xFF; 
    
    while (1) 
    {
        for (int i = 0; i <= 255; i++)
        {
            PORTB = i;
            _delay_ms(50); 
        }
    }
    
    return 0;
}
