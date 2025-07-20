B/*
 * DEMO_1.c
 *
 * Created: 07-02-2024 17:28:24
 * Author : online
 */ 

 /*
  * Experiment_2_Task_1.c
  *
  * Created: 06-02-2024 21:54:55
  * Author : Aryan
  */

#include <avr/io.h>
#include <util/delay.h>
#define F_CPU 16000000UL;

void Pattern_0() {
    PORTB = 0xFF;
    _delay_ms(500);
    PORTB = 0x00;
    _delay_ms(500);
}

void Pattern_1() {
    PORTB = 0xAA;
    _delay_ms(500);
    PORTB = 0x55;
    _delay_ms(500);
}

void Pattern_2() {
    PORTB = 0xF0;
    _delay_ms(500);
    PORTB = 0x0F;
    _delay_ms(500);
}

void Pattern_3() {
    PORTB = 0x00;
    _delay_ms(500);
    PORTB = 0x01;

    while (PORTB != 0x00) {
        _delay_ms(500);
        PORTB = PORTB << 1;

        if (PORTB == 0xFF) {
            PORTB == 0x01;
        }
    }
}

void Pattern_4() {
    PORTB = 0xFF;
    _delay_ms(500);
    int Sequences[8] = { 0xFE,0xFD,0xFB,0xF7,0xEF,0xDF,0xBF,0x7F };

    int i = 0;
    while (i <= 9) {
        PORTB = Sequences[i];
        _delay_ms(500);

        if (i == 9) {
            i = -1;
            PORTB = 0xFF;
            _delay_ms(500);
        }
        i++;
    }
}

void Pattern_5() {
    PORTB = 0x00;
    _delay_ms(500);
    PORTB = 0x80;

    while (PORTB != 0x00) {
        _delay_ms(500);
        PORTB = PORTB >> 1;

        if (PORTB == 0x01) {
            PORTB == 0x80;
        }
    }
}

void Pattern_6() {
    PORTB = 0x00;
    _delay_ms(500);
    int Sequences[7] = { 0x81,0x42,0x24,0x18,0x24,0x42,0x81 };

    int i = 0;
    while (i <= 7) {
        PORTB = Sequences[i];
        _delay_ms(500);
        i++;

        if (i == 8) {
            i = 0;
        }
    }
}

void Pattern_7() {
    PORTB = 0x7F;
}

void Pattern_8() {
    PORTB = 0xFF;
}

void Pattern_9() {
    PORTB = 0x00;
}

int main(void)
{
    /* Replace with your application code */
    DDRB = 0xFF;

    while (1) {
            /*Pattern_0();
			_delay_ms(500);
            Pattern_1();
			_delay_ms(500);
            Pattern_2();
			_delay_ms(500);
            Pattern_3();
			_delay_ms(500);
            Pattern_4();
			_delay_ms(500);
            Pattern_5();
			_delay_ms(500);
            Pattern_6();
			_delay_ms(500);
            Pattern_7();
			_delay_ms(500);
            Pattern_8();
			_delay_ms(500); */
            Pattern_9();
			_delay_ms(500);
    }
}



