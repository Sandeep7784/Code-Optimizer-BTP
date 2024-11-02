int calculate_register_value() {
    return (*reg) * 2;
}

#include <stdio.h>

void perform_calculation() {
    printf("Register value calculation result: %d\n", calculate_register_value());
}

void set_register_value(uint32_t value) {
    *(volatile uint32_t *)REG_ADDR = value;
}

uint32_t get_register_value() {
    return *(__volatile uint32_t*)REG_ADDR;
}

int main() {
    uint32_t reg_value = set_register_value(10);
    printf("Current register value: %u\n", reg_value);
    return 0;
}