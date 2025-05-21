#pragma once

#include "esphome/components/spi/spi.h"
#include "esphome/core/component.h"
#include "esphome/core/hal.h"

namespace esphome {
namespace max4820 {

class MAX4820 : public Component,
                public spi::SPIDevice<spi::BIT_ORDER_MSB_FIRST, spi::CLOCK_POLARITY_LOW, spi::CLOCK_PHASE_LEADING,
                                      spi::DATA_RATE_75KHZ> {  // Running at the slowest max speed supported by the
                                                               // max4820. 2.7v = 75ksps
 public:
  void setup() override;
  void dump_config() override;
  float get_setup_priority() const override;

  bool get_switch_state(uint8_t switch_id);
  void set_switch_state(uint8_t switch_id, bool state);

protected:
  uint8_t states = 0;
};

}  // namespace max4820
}  // namespace esphome
