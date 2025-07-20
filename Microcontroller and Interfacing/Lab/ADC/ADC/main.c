/*
 * ADC.c
 *
 * Created: 26-03-2024 13:59:39
 * Author : online
 */ 

#define F_CPU 8000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <string.h>
#include <stdio.h>

#define degree_sysmbol 0xdf

void LCD_Init() {
	_delay_ms(50); // wait for LCD to power up
	LCD_Command(0x38); // Initialize 8-bit mode
	LCD_Command(0x0C); // Display ON, Cursor OFF
	LCD_Command(0x06); // Increment cursor
	LCD_Command(0x01); // Clear LCD
	_delay_ms(2); // Delay for LCD to clear
	LCD_Command(0x80); // Move cursor to beginning of first line
}

void LCD_Command(unsigned char Command) {
	PORTB = Command;
	PORTC &= ~(0x01);
	PORTC &= ~(0x02);
	PORTC |= (0x04);
	_delay_ms(1); // Increased delay for commands
	PORTC &= ~(0x04);
}

void LCD_Data(unsigned char Data) {
	PORTB = Data;
	PORTC |= (0x01);
	PORTC &= ~(0x02);
	PORTC |= (0x04);
	_delay_ms(1); // Increased delay for data
	PORTC &= ~(0x04);
}


void ADC_Init(){
	DDRA = 0x00;	        /* Make ADC port as input */
	ADCSRA = 0x87;          /* Enable ADC, with freq/128  */
	ADMUX = 0x40;           /* Vref: Avcc, ADC channel: 0 */
}


int ADC_Read(char channel)
{
	ADMUX = 0x40 | (channel & 0x07);   /* set input channel to read */
	ADCSRA |= (1<<ADSC);               /* Start ADC conversion */
	while (!(ADCSRA & (1<<ADIF)));     /* Wait until end of conversion by polling ADC interrupt flag */
	ADCSRA |= (1<<ADIF);               /* Clear interrupt flag */
	_delay_ms(1);                      /* Wait a little bit */
	return ADCW;                       /* Return ADC word */
}

void LCD_String_xy(uint8_t row, uint8_t col, const char *str) {
	uint8_t position = 0;
	
	if (row == 1)
	position = 0x80 + col;      // If row 1, calculate position
	else if (row == 2)
	position = 0xC0 + col;      // If row 2, calculate position
	
	LCD_Command(position);          // Set cursor position
	while (*str) {
		LCD_Data(*str);             // Send data byte by byte
		str++;
	}
}

int main()
{
	char Temperature[10];
	float celsius;

	LCD_Init();                 /* initialize 16x2 LCD*/
	ADC_Init();                 /* initialize ADC*/
	
	while(1)
	{
		LCD_String_xy(1,0,"Temperature");
		celsius = (ADC_Read(0)*4.88);
		celsius = (celsius/10.00);
		sprintf(Temperature,"%d%cC  ", (int)celsius, degree_sysmbol);
		LCD_String_xy(2,0,Temperature);
		_delay_ms(1000);
		memset(Temperature,0,10);
	}
}


