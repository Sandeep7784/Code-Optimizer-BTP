#define LED_PIN 5
#define PORT_A_DIR (*(volatile uint32_t *)0x40020000)
#define PORT_A_OUT (*(volatile uint32_t *)0x40020014)void optimized_delay_ms(int ms)
{
    volatile uint32_t count;
    while (ms--)
    {
        count = PORT_A_DIR;
        for (count = 0; count < 1000; count++)
        {
            // Do nothing, just waste time
        }
        PORT_A_DIR = count;
    }
}

while (1)
{
    PORT_A_OUT = (1 << LED_PIN);
    PORT_A_DIR |= (1 << LED_PIN);
    __delay_cycles(5000000);
    PORT_A_DIR &= ~(1 << LED_PIN);
}

void set_led_pin_as_output(void) {
    *(volatile uint32_t *)0x40020000 |= (1 << 5);
}

{
    printf("Starting main...\n");
    init_hardware();
    while (1) {
        PORT_A_DIR |= (1 << LED_PIN);
        delay_ms(1000);
        PORT_A_DIR &= ~(1 << LED_PIN);
        delay_ms(1000);
    }
    printf("Main finished.\n"); // This line will never be reached
    return 0;
}