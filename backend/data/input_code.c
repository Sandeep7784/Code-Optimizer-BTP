#include <stdio.h>
#include <stdint.h>

// Global declarations
#define LED_PIN 5
#define PORT_A_DIR (*(volatile uint32_t *)0x40020000)
#define PORT_A_OUT (*(volatile uint32_t *)0x40020014)

// Function prototypes
void blink_led(void);
void unused_function(void);
void infinite_loop(void);
void delay_ms(uint32_t ms);

// Function 1: Delay function
void delay_ms(uint32_t ms)
{
    volatile uint32_t count;
    while (ms--)
    {
        for (count = 0; count < 1000; count++)
        {
            // Do nothing, just waste time
        }
    }
}

// Function 2: Infinite loop function
void infinite_loop(void)
{
    while (1)
    {
        blink_led();
    }
}

// Function 3: Initialize hardware
void init_hardware(void)
{
    // Set Port A, Pin 5 as output
    PORT_A_DIR |= (1 << LED_PIN);
}

int main()
{
    printf("Starting main...\n");
    init_hardware();
    infinite_loop();
    printf("Main finished.\n"); // This line will never be reached
    return 0;
}