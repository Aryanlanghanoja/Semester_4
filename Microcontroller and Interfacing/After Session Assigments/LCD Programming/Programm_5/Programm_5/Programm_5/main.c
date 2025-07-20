/*
 * Programm_5.c
 *
 * Created: 18-02-2024 20:39:56
 * Author : Aryan
 */ 

#define F_CPU 8000000UL
#include <avr/io.h>
#include <util/delay.h>
#define rs PB2
#define en PB3

void lcd_init();
void dis_cmd(char);
void dis_data(char);
void lcdcmd(char);
void lcddata(char);
void lcd_create_custom_char();
void lcd_display_custom_char();

int main(void)
{
	DDRB = 0xFF;
	lcd_init();

	lcd_create_custom_char();
	lcd_display_custom_char();

	while (1)
	{
		// Your main code here
	}
}

void lcd_init()
{
	dis_cmd(0x02);
	dis_cmd(0x28);
	dis_cmd(0x01);
	dis_cmd(0x0C);
	dis_cmd(0x06);
	dis_cmd(0x80); // Set DDRAM address to 0 (cursor at home position)
}

void dis_cmd(char cmd_value)
{
	char cmd_value1;
	cmd_value1 = cmd_value & 0xF0;
	lcdcmd(cmd_value1);

	cmd_value1 = ((cmd_value << 4) & 0xF0);
	lcdcmd(cmd_value1);
}

void dis_data(char data_value)
{
	char data_value1;
	data_value1 = data_value & 0xF0;
	lcddata(data_value1);

	data_value1 = ((data_value << 4) & 0xF0);
	lcddata(data_value1);
}

void lcdcmd(char cmdout)
{
	PORTB = cmdout;
	PORTB &= ~(1 << rs);
	PORTB |= (1 << en);
	_delay_ms(1);
	PORTB &= ~(1 << en);
}

void lcddata(char dataout)
{
	PORTB = dataout;
	PORTB |= (1 << rs);
	PORTB |= (1 << en);
	_delay_ms(1);
	PORTB &= ~(1 << en);
}

void lcd_create_custom_char()
{
	// Set CGRAM address to 0
	dis_cmd(0x40);

	// Define custom character pattern (Heart shape)
	dis_data(0b00000);
	dis_data(0b01010);
	dis_data(0b11111);
	dis_data(0b11111);
	dis_data(0b01110);
	dis_data(0b00100);
	dis_data(0b00000);
	dis_data(0b00000);

	// Set DDRAM address to 0x80 (cursor at home position)
	dis_cmd(0x80);
	_delay_ms(100);
}

void lcd_display_custom_char()
{
	// Display the custom character at the beginning of the first line
	dis_data(0); // Display custom character at position (0, 0)
}

