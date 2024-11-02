#include <stdint.h>

#define REG_BASE_ADDR 0x40000000
#define REG_OFFSET 0x10
#define REG_ADDR (REG_BASE_ADDR + REG_OFFSET)

volatile uint32_t *reg = (volatile uint32_t *)REG_ADDR;

void unused_function() {
    // This function is never called
    printf("This is an unused function.\n");
}

int unused_variable = 42;

int calculate_register_value() {
    return *reg * 2;
}

void perform_calculation() {
    int result = calculate_register_value();
    printf("Register value calculation result: %d\n", result);
}

perform_calculation();
void set_register_value(uint32_t value) {
    *reg = value;
}

uint32_t get_register_value() {
    return *reg;
}

int main() {
    set_register_value(10);
    perform_calculation();
    uint32_t reg_value = get_register_value();
    printf("Current register value: %u\n", reg_value);
    return 0;
}