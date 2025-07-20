/*
 * Programm_2.c
 *
 * Created: 18-02-2024 14:39:14
 * Author : Aryan Langhanoja
 */ 

#include <avr/io.h>
#include <util/delay.h>

#define F_CPU 1000000UL

void LCD_Command(unsigned char Command) {
	
	unsigned char A , B ;
	A = Command & 0xF0 ;
	PORTB = A | 0x04 ;
	_delay_ms(100);
	PORTB &= ~(0x04) ;
	
	B = Command << 4 ;
	PORTB = B | 0x04 ;
	_delay_ms(100) ;
	PORTB &= ~(0x04) ;
}

void LCD_Data(unsigned char Data) {

	unsigned char A,B ;
	A = Data & 0xF0 ;
	PORTB = 0x05  | A ;
	_delay_ms(100) ;
	PORTB &= ~(0x04) ;
	
	B = Data << 4 ;
	PORTB = 0x05  | B ;
	_delay_ms(100) ;
	PORTB &= ~(0x04) ;
}

void LCD_SetCursor(uint8_t row, uint8_t column) {
	uint8_t position = 0x80;

	if (row == 1)
	position = 0xC0;

	position += column - 1; 
	LCD_Command(position);
}

int main(void) {
	DDRB = 0x0F ;

	LCD_Command(0x02);
	LCD_Command(0x28);
	LCD_Command(0x0E);
	LCD_Command(0x06);
	LCD_Command(0x01);
	LCD_Command(0x80);
	
	char First_Name[5] = "ARYAN";
	char Last_Name[10] = "LANGHANOJA";
	
	LCD_SetCursor(0, 5);
	for (int i = 0; i < 5; i++) {
		LCD_Data(First_Name[i]);
	}

	LCD_SetCursor(1, 3);
	for (int i = 0; i < 10; i++) {
		LCD_Data(Last_Name[i]);
	}
	
	while (1);
	
	return 0;
}



