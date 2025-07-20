/*
 * Programm_1.c
 *
 * Created: 18-02-2024 13:53:05
 * Author : Aryan
 */ 

#include <avr/io.h>
#include <util/delay.h>
#define F_CPU 1000000UL

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

void LCD_Init() {
	_delay_ms(50); // wait for LCD to power up
	LCD_Command(0x38); // Initialize 8-bit mode
	LCD_Command(0x0C); // Display ON, Cursor OFF
	LCD_Command(0x06); // Increment cursor
	LCD_Command(0x01); // Clear LCD
	_delay_ms(2); // Delay for LCD to clear
	LCD_Command(0x80); // Move cursor to beginning of first line
}

void LCD_SetCursor(uint8_t row, uint8_t column) {
	uint8_t position = 0x80; // Base address for the first line

	if (row == 1) // If second row
		position = 0xC0; // Base address for the second line

	position += column - 1; // Adjust position for the desired column
	LCD_Command(position); // Set cursor position
}

int main(void) {
	DDRB = 0xFF;
	DDRC = 0xFF;
	LCD_Init(); 
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

