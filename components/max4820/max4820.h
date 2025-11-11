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

  void set_reset_pin(InternalGPIOPin *reset_pin) { this->reset_pin_ = reset_pin; }
  void set_set_pin(InternalGPIOPin *set_pin) { this->set_pin_ = set_pin; }
  void set_sr_num(uint8_t sr_num) { this->sr_num_ = sr_num; }

  bool get_switch_state(uint8_t switch_id);
  void set_switch_state(uint8_t switch_id, bool state);

protected:
  InternalGPIOPin *reset_pin_{nullptr};
  InternalGPIOPin *set_pin_{nullptr};
  uint8_t sr_num_{1};

  uint8_t states = 0;

  void reset_device_();
};

}  // namespace max4820
}  // namespace esphome
