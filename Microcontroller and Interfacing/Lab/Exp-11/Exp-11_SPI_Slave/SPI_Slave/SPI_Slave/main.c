/*
 * SPI_Slave.c
 *
 * Created: 09-04-2024 15:07:39
 * Author : online
 */ 

#define F_CPU 8000000UL			/* Define CPU Frequency 8MHz */
#include <avr/io.h>			/* Include AVR std. library file */
#include <util/delay.h>			/* Include Delay header file */
#include <stdio.h>			/* Include std. i/p o/p file */
#include <string.h>			/* Include string header file */
#include "LCD_16x2_C_file-1.c"
#include "LCD_16x2_H_file-1.h"
#include "SPI_Slave_C_file.c"
#include "SPI_Slave_H_file.h"
#include "LCD_16x2_H_file.h"

int main(void)
{
	uint8_t count;
	char buffer[5];
	
	LCD_Init();
	SPI_Init();
	
	LCD_String_xy(1, 0, "Slave Device");
	LCD_String_xy(2, 0, "Receive Data:    ");
	while (1)			/* Receive count continuous */
	{
		count = SPI_Receive();
		sprintf(buffer, "%d   ", count);
		LCD_String_xy(2, 13, buffer);
	}

}


