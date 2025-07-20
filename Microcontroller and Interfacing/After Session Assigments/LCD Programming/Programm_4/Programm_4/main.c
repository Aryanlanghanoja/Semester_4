/*
 * Programm_4.c
 *
 * Created: 18-02-2024 16:30:44
 * Author : Aryan
 */ 

#include <avr/io.h>
#include <util/delay.h>
#include <string.h>
#define LCD_RS PA0
#define LCD_RW PA1
#define LCD_EN PA2
#define LCD_DATA_PORT PORTB

void lcd_cmd(unsigned char cmd) {
	LCD_DATA_PORT = (cmd & 0xF0); // Send higher nibble
	PORTA &= ~(1 << LCD_RS); // Set RS to command mode
	PORTA &= ~(1 << LCD_RW); // Set RW to write mode
	PORTA |= (1 << LCD_EN); // Enable LCD
	_delay_ms(1);
	PORTA &= ~(1 << LCD_EN); // Disable LCD

	LCD_DATA_PORT = ((cmd << 4) & 0xF0); // Send lower nibble
	PORTA |= (1 << LCD_EN); // Enable LCD
	_delay_ms(1);
	PORTA &= ~(1 << LCD_EN); // Disable LCD
}
void lcd_data(unsigned char data) {
	LCD_DATA_PORT = (data & 0xF0); // Send higher nibble
	PORTA |= (1 << LCD_RS); // Set RS to data mode
	PORTA &= ~(1 << LCD_RW); // Set RW to write mode
	PORTA |= (1 << LCD_EN); // Enable LCD
	_delay_ms(1);
	PORTA &= ~(1 << LCD_EN); // Disable LCD

	LCD_DATA_PORT = ((data << 4) & 0xF0); // Send lower nibble
	PORTA |= (1 << LCD_EN); // Enable LCD
	_delay_ms(1);
	PORTA &= ~(1 << LCD_EN); // Disable LCD
}
void lcd_init() {
	lcd_cmd(0x02); // Initialize LCD in 4-bit mode
	lcd_cmd(0x28); // 2 lines, 5x7 dots, 4-bit mode
	lcd_cmd(0x0C); // Display ON, cursor OFF
	lcd_cmd(0x06); // Entry mode: Increment cursor
	lcd_cmd(0x80); // Set cursor to beginning of first line
}
void scroll_text(const char* text, int direction) {
	int len = strlen(text);
	int start = (direction == 0) ? 0 : len - 16;

	for (int i = start; i >= 0 && i <= len - 16; i += (direction == 0) ? 1 : -1) {
		lcd_cmd(0x80);
		for (int j = 0; j < 16; j++) {
			lcd_data(text[i + j]);
		}
		_delay_ms(300);
	}
}
int main(void) {
	DDRA = 0xFF;
	DDRB = 0xFF;
	DDRD &= ~((1 << PD0) | (1 << PD1));

	lcd_init();

	while (1) {
		if (!(PIND & (1 << PD0))) {
			scroll_text("HELLO FROM ARYAN LANGHANOJA", 0);
			} else if (!(PIND & (1 << PD1))) {
			scroll_text("HELLOVFROM ARYAN LANGHANOJA", 1);
		}
	}
}