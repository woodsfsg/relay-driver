#include "max4820.h"

#include "esphome/core/helpers.h"
#include "esphome/core/log.h"

namespace esphome {
namespace max4820 {

static const char *const TAG = "max4820";

float MAX4820::get_setup_priority() const { return setup_priority::BUS; }

void MAX4820::setup() {
  ESP_LOGCONFIG(TAG, "Setting up max4820");
  this->states = 0;
  
  this->spi_setup();
  
  if (this->reset_pin_ != nullptr) {
    this->reset_pin_->setup();
    this->reset_device_();
  }
  
  this->enable();
  this->write_byte(states);
  this->disable();
}

void MAX4820::reset_device_() {
  this->states = 0;
  if (this->reset_pin_ != nullptr) {
    ESP_LOGD(TAG, "Reset device using RESET pin");
    this->reset_pin_->digital_write(false);
    delay(1);
    this->reset_pin_->digital_write(true);
  } else {
    ESP_LOGD(TAG, "Reset device using SWRST command");
    this->set_switch_state(0,false);
  }
}

void MAX4820::dump_config() {
  ESP_LOGCONFIG(TAG, "MAX4820:");
  LOG_PIN("   CS Pin:", this->cs_);
  if (this->reset_pin_ != nullptr) {
      LOG_PIN("Reset Pin:", this->reset_pin_);
  }
}

bool MAX4820::get_switch_state(uint8_t switch_id) {
  return (states >> switch_id) & 0b1;
}

void MAX4820::set_switch_state(uint8_t switch_id, bool state) {
  states = (states & (0xff ^ (0b1 << switch_id))) | (((state ? 0b1 : 0) << switch_id));
  
  this->enable();
  this->write_byte(states);
  this->disable();
  
  ESP_LOGD(TAG, "Switch state: 0x%02X", states);
}

}  // namespace max4820
}  // namespace esphome
