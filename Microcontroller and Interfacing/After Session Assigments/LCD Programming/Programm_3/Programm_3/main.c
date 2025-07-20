/*
 * Programm_3.c
 *
 * Created: 18-02-2024 15:32:15
 * Author : Aryan 
 */ 

#include <avr/io.h>
#include <util/delay.h>

#define LCD_DATA_PORT PORTD
#define LCD_CTRL_PORT PORTC
#define LCD_RS PC0
#define LCD_RW PC1
#define LCD_EN PC2

void LCD_Command(unsigned char Command) {
	LCD_DATA_PORT = (LCD_DATA_PORT & 0x0F) | (Command & 0xF0);
	LCD_CTRL_PORT &= ~(1 << LCD_RS); // RS low for command
	LCD_CTRL_PORT &= ~(1 << LCD_RW); // RW low for write
	LCD_CTRL_PORT |= (1 << LCD_EN); // Enable high
	_delay_us(1);
	LCD_CTRL_PORT &= ~(1 << LCD_EN); // Enable low
	_delay_us(100);
	
	LCD_DATA_PORT = (LCD_DATA_PORT & 0x0F) | ((Command << 4) & 0xF0);
	LCD_CTRL_PORT |= (1 << LCD_EN); // Enable high
	_delay_us(1);
	LCD_CTRL_PORT &= ~(1 << LCD_EN); // Enable low
	_delay_ms(2);
}

void LCD_Data(unsigned char Data) {
	LCD_DATA_PORT = (LCD_DATA_PORT & 0x0F) | (Data & 0xF0);
	LCD_CTRL_PORT |= (1 << LCD_RS); // RS high for data
	LCD_CTRL_PORT &= ~(1 << LCD_RW); // RW low for write
	LCD_CTRL_PORT |= (1 << LCD_EN); // Enable high
	_delay_us(1);
	LCD_CTRL_PORT &= ~(1 << LCD_EN); // Enable low
	_delay_us(100);
	
	LCD_DATA_PORT = (LCD_DATA_PORT & 0x0F) | ((Data << 4) & 0xF0);
	LCD_CTRL_PORT |= (1 << LCD_EN); // Enable high
	_delay_us(1);
	LCD_CTRL_PORT &= ~(1 << LCD_EN); // Enable low
	_delay_ms(2);
}

void LCD_Init(void) {
	LCD_DATA_PORT = 0xFF; // Initialize LCD data port as output
	LCD_CTRL_PORT |= (1 << LCD_EN) | (1 << LCD_RW) | (1 << LCD_RS); // Initialize control port pins as output
	_delay_ms(20);
	
	LCD_Command(0x33); // Initialization sequence
	LCD_Command(0x32); // Initialization sequence
	LCD_Command(0x28); // 4-bit mode, 2 lines, 5x8 font
	LCD_Command(0x0C); // Display on, cursor off, blink off
	LCD_Command(0x06); // Increment cursor
	LCD_Command(0x01); // Clear display
	_delay_ms(2);
}

void LCD_Clear(void) {
	LCD_Command(0x01); // Clear display
	_delay_ms(2);
}

void LCD_GotoXY(unsigned char x, unsigned char y) {
	unsigned char address = 0;
	if (y == 0) {
		address = 0x80 + x; // Line 1
		} else if (y == 1) {
		address = 0xC0 + x; // Line 2
	}

	LCD_Command(address);
}


void LCD_Puts(const char *str) {
	while (*str) {
		LCD_Data(*str++);
	}
}
// right to left
void LCD_Scroll_Text(const char *text) {
	int len = 0;
	while (text[len] != '\0') {
		len++;
	}
	
	// Calculate the starting position
	int start_position = len > 16 ? len - 16 : 0;

	// Add spaces at the beginning to adjust the starting position
	char scrolled_text[2 * len + 6]; // Double the length of the text for scrolling effect
	for (int i = 0; i < start_position; i++) {
		scrolled_text[i] = ' ';
	}

	// Copy the text to scrolled_text
	for (int i = 0; i < len; i++) {
		scrolled_text[start_position + i] = text[i];
	}

	while (1) {
		for (int i = 0; i < len + start_position + 3; i++) {
			LCD_Clear();
			LCD_GotoXY(0, 0);
			LCD_Puts(scrolled_text + i);
			_delay_ms(500); // Adjust the delay as needed for desired scrolling speed
		}
	}
}


int main(void) {
	DDRD = 0xFF; // Port D as output
	DDRC |= (1 << LCD_EN) | (1 << LCD_RW) | (1 << LCD_RS); // Control pins as output
	
	LCD_Init();
	LCD_Clear();
	
	LCD_Scroll_Text("HELLO FROM ARYAN LANGHANOJA");
	
	while (1) {
	}
	
	return 0;
}




