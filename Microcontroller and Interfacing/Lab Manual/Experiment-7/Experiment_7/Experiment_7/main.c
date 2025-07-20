/*
 * Experiment_7.c
 *
 * Created: 16-03-2024 14:34:58
 * Author : online
 */ 

#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#define LCD PORTA
// LCD data port connected to PORTC
#define EN 7
#define RW 6
#define RS 5

unsigned char keypad();
void lcdcmd(unsigned char cmd)
{
	PORTD &= ~(1 << RS); // RS=0 for command
	PORTD &= ~(1 << RW); // RW=0 for write
	LCD = cmd & 0xF0; // send upper nibble
	PORTD |= (1 << EN); // EN=1 for H to L pulse
	_delay_ms(1);
	PORTD &= ~(1 << EN); // EN=0 for H to L pulse
	LCD = cmd << 4; // send low nibble
	PORTD |= (1 << EN); // EN=1 for H to L pulse
	_delay_ms(1);
	PORTD &= ~(1 << EN);
}
void lcddata(unsigned char data)
{
	PORTD |= (1 << RS); // RS=1 for data //RW=0 for write
	PORTD &= ~(1 << RW);
	LCD = data & 0xF0; // send upper nibble
	PORTD |= (1 << EN); // EN=1 for H to L pulse
	_delay_ms(1);
	PORTD &= ~(1 << EN); // EN=0 for H to L pulse
	LCD = data << 4; // send low nibble
	PORTD |= (1 << EN); // EN=1 for H to L pulse
	_delay_ms(1);
	PORTD &= ~(1 << EN);
}
void lcd_init(){
	DDRA = 0xFF; // define output LCD port
	DDRD = 0xFF; // define RS,EN and RW pin as output
	PORTD &= ~(1 << EN); // initialize en = 0
	lcdcmd(0x33);
	lcdcmd(0x32);
	lcdcmd(0x28); // LCD in 4 bit mode
	lcdcmd(0x0E); // display on cursor on
	lcdcmd(0x01); // clear LCD
	_delay_ms(2);
}
int main(void)
{
	unsigned char x;
	DDRC = 0x0F; // Make PCO to PC3 = O/P and PC4 to PC7 = 1/P
	_delay_ms(1);
	PORTC = 0xF0;
	lcd_init();
	while (1)
	{
		PORTC = 0xF0; // Make all 4 columns 1 and all 4 rows 0
		_delay_ms(25);
		if (PINC != 0xF0)
		{
			x = keypad();
			lcddata(x);
		}
}
return 0;
}
unsigned char keypad()
{
	PORTC = 0b11111110; // make first row 0
	if ((PINC & (1 << PINC4)) == 0)
	{
		_delay_ms(125);
		return '7';
	}
	else if ((PINC & (1 << PINC5)) == 0)
	{
		_delay_ms(125);
		return '8';
	}
	else if ((PINC & (1 << PINC6)) == 0)
	{
		_delay_ms(125);
		return '9';
	}
	else if ((PINC & (1 << PINC7)) == 0)
	{
		_delay_ms(125);
		return '/';
	}
	PORTC = 0b11111101; // make second row 0
	 if ((PINC & (1 << PINC4)) == 0)
	 {
		 _delay_ms(125);
		 return '4';
	 }
	 else if ((PINC & (1 << PINC5)) == 0)
	 {
		 _delay_ms(125);
		 return '5';
	 }
	 else if ((PINC & (1 << PINC6)) == 0)
	 {
		 _delay_ms(125);
		 return '6';
	 }
	 else if ((PINC & (1 << PINC7)) == 0)
	 {
		 _delay_ms(125);
		 return '*';
	 }
	 PORTC = 0b11111011; // make third row 0
	 if ((PINC & (1 << PINC4)) == 0)
	 {
		 _delay_ms(125);
		 return '1';
	 }
	 else if ((PINC & (1 << PINC5)) == 0)
	 {
		 _delay_ms(125);
		 return '2';
	  }
	  else if ((PINC & (1 << PINC6)) == 0)
	  {
		  _delay_ms(125);
		  return '3';
	  }
	  else if ((PINC & (1 << PINC7)) == 0)
	  {
		  _delay_ms(175);
		  return '-';
	  }
	  PORTC = 0b11110111; // make forth row 0
	  if ((PINC & (1 << PINC4)) == 0)
	  {
		  _delay_ms(125);
		  return 'C';
	  }
	  else if ((PINC & (1 << PINC5)) == 0)
	  {
		  _delay_ms(125);
		  return '0';
	  }
	  else if ((PINC & (1 << PINC6)) == 0)
	  {
		  _delay_ms(125);
		  return '=';
	  }
	  else if ((PINC & (1 << PINC7)) == 0)
	  {
		  _delay_ms(125);
		   return '+';
	   }
	   return 0;
   }



