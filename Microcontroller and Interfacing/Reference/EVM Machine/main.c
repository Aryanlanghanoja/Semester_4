#include "LCD16x2_4bit.h"
#include <avr/io.h>
#include <util/delay.h>

#define KEY_PRT PORTA
#define KEY_DDR	DDRA
#define KEY_PIN	PINA

unsigned char keypad[4][4] = {
    {' ',' ','Q','B'},
    {' ',' ',' ','C'},
    {' ',' ',' ','A'},
    {' ',' ',' ','N'}};

unsigned char colloc, rowloc;

char keyfind() {
    while(1) {
        KEY_DDR = 0xF0;           
        KEY_PRT = 0xFF;
        
        do {
            KEY_PRT &= 0x0F;
            asm("NOP");
            colloc = (KEY_PIN & 0x0F);
        } while(colloc != 0x0F);
        
        do {
            do {
                _delay_ms(20);     
                colloc = (KEY_PIN & 0x0F); 
            } while(colloc == 0x0F);        
            _delay_ms(40);	            
            colloc = (KEY_PIN & 0x0F);
        } while(colloc == 0x0F);

        KEY_PRT = 0xEF;            
        asm("NOP");
        colloc = (KEY_PIN & 0x0F);
        if(colloc != 0x0F) {
            rowloc = 0;
            break;
        }
        
        KEY_PRT = 0xDF;		
        asm("NOP");
        colloc = (KEY_PIN & 0x0F);
        if(colloc != 0x0F) {
            rowloc = 1;
            break;
        }
        
        KEY_PRT = 0xBF;		
        asm("NOP");
        colloc = (KEY_PIN & 0x0F);
        if(colloc != 0x0F) {
            rowloc = 2;
            break;
        }

        KEY_PRT = 0x7F;		
        asm("NOP");
        colloc = (KEY_PIN & 0x0F);
        if(colloc != 0x0F) {
            rowloc = 3;
            break;
        }
    }

    if(colloc == 0x0E)
        return(keypad[rowloc][0]);
    else if(colloc == 0x0D)
        return(keypad[rowloc][1]);
    else if(colloc == 0x0B)
        return(keypad[rowloc][2]);
    else
        return(keypad[rowloc][3]);
}

int main(void) {
    int arr[] = {0,0,0,0};
    char vote;
    LCD_Init();
    LCD_String_xy(1,0,"You Voted:");
    while(1) {
        LCD_Command(0xC0);
        vote = keyfind();
        switch (vote) {
            case 'B':
                arr[0]++;
                LCD_Clear(); // Clear the display before updating
                LCD_String_xy(2,1,"BJP");   
                _delay_ms(100);
                break;
            case 'C':
                arr[1]++;
                LCD_Clear();
                LCD_String_xy(2,1,"CON");
                _delay_ms(100);
                break;
            case 'A':
                arr[2]++;
                LCD_Clear();
                LCD_String_xy(2,1,"AAP");
                _delay_ms(100);
                break;
            case 'N':
                arr[3]++;
                LCD_Clear();
                LCD_String_xy(2,1,"NOTA");
                _delay_ms(100);
                break;
            case 'Q':
                LCD_Clear();
                LCD_String_xy(1,0,"BJP");
                LCD_String_xy(2,1,arr[0]);
                _delay_ms(100);
                LCD_Clear();
                LCD_String_xy(1,0,"CON");
                LCD_String_xy(2,1,arr[1]);
                _delay_ms(100);
                LCD_Clear();
                LCD_String_xy(1,0,"AAP");
                LCD_String_xy(2,1,arr[2]);
                _delay_ms(100);
                LCD_Clear();
                LCD_String_xy(1,0,"NOTA");
                LCD_String_xy(2,1,arr[3]);
                _delay_ms(100);
                LCD_Clear();
                break;
        }
    }
}

