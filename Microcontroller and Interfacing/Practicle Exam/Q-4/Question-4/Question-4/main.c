#include <avr/io.h>
#include <util/delay.h>

#define LCD PORTA
#define EN 7
#define RW 6
#define RS 5

unsigned char keypad();

void lcdcmd(unsigned char cmd) {
	PORTD &= ~(1 << RS);
	PORTD &= ~(1 << RW);
	LCD = cmd & 0xF0;
	PORTD |= (1 << EN);
	_delay_ms(10);
	PORTD &= ~(1 << EN);
	LCD = cmd << 4;
	PORTD |= (1 << EN);
	_delay_ms(1);
	PORTD &= ~(1 << EN);
}

void lcddata(unsigned char data) {
	PORTD |= (1 << RS);
	PORTD &= ~(1 << RW);
	LCD = data & 0xF0;
	PORTD |= (1 << EN);
	_delay_ms(10);
	PORTD &= ~(1 << EN);
	LCD = data << 4;
	PORTD |= (1 << EN);
	_delay_ms(1);
	PORTD &= ~(1 << EN);
}

void lcd_init() {
	DDRA = 0xFF;
	DDRD = 0xFF;
	PORTD &= ~(1 << EN);
	lcdcmd(0x33);
	lcdcmd(0x32);
	lcdcmd(0x28);
	lcdcmd(0x0E);
	lcdcmd(0x01);
	_delay_ms(2);
}

unsigned char keypad() {
	PORTC = 0b11111110;
	if ((PINC & (1 << PINC4)) == 0) {
		_delay_ms(125);
		return '7';
	}
	else if ((PINC & (1 << PINC5)) == 0) {
		_delay_ms(125);
		return '8';
	}
	else if ((PINC & (1 << PINC6)) == 0) {
		_delay_ms(125);
		return '9';
	}
	else if ((PINC & (1 << PINC7)) == 0) {
		_delay_ms(125);
		return '/';
	}
	PORTC = 0b11111101;
	if ((PINC & (1 << PINC4)) == 0) {
		_delay_ms(125);
		return '4';
	}
	else if ((PINC & (1 << PINC5)) == 0) {
		_delay_ms(125);
		return '5';
	}
	else if ((PINC & (1 << PINC6)) == 0) {
		_delay_ms(125);
		return '6';
	}
	else if ((PINC & (1 << PINC7)) == 0) {
		_delay_ms(125);
		return '*';
	}
	PORTC = 0b11111011;
	if ((PINC & (1 << PINC4)) == 0) {
		_delay_ms(125);
		return '1';
	}
	else if ((PINC & (1 << PINC5)) == 0) {
		_delay_ms(125);
		return '2';
	}
	else if ((PINC & (1 << PINC6)) == 0) {
		_delay_ms(125);
		return '3';
	}
	else if ((PINC & (1 << PINC7)) == 0) {
		_delay_ms(175);
		return '-';
	}
	PORTC = 0b11110111;
	if ((PINC & (1 << PINC4)) == 0) {
		_delay_ms(125);
		return 'C';
	}
	else if ((PINC & (1 << PINC5)) == 0) {
		_delay_ms(125);
		return '0';
	}
	else if ((PINC & (1 << PINC6)) == 0) {
		_delay_ms(125);
		return '=';
	}
	else if ((PINC & (1 << PINC7)) == 0) {
		_delay_ms(125);
		return '+';
	}
	return 0;
}

int main(void) {
	unsigned char x;
	DDRC = 0x0F;
	_delay_ms(1);
	PORTC = 0xF0;
	lcd_init();
	PORTC = 0xF0;
	_delay_ms(25);
	if (PINC != 0xF0) {
		char password[4] = "123x";
		int correct = 0;

		for (int i = 0; i < 4; i++) {
			x = keypad();
			lcddata(x);

			if (x == password[i]) {
				correct++;
			}
		}

		if (correct == 4) {
			char output[] = "Correct Password";

			for (int i = 0; i < sizeof(output) / sizeof(output[0]); i++) {
				lcddata(output[i]);
			}
		}
		else {
			char output[] = "Incorrect Password";

			for (int i = 0; i < sizeof(output) / sizeof(output[0]); i++) {
				lcddata(output[i]);
			}
		}
	}

	return 0;
}
