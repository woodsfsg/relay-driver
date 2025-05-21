#include "max4820.h"

#include "esphome/core/helpers.h"
#include "esphome/core/log.h"

namespace esphome {
namespace max4820 {

static const char *const TAG = "max4820";

float MAX4820::get_setup_priority() const { return setup_priority::HARDWARE; }

void MAX4820::setup() {
  ESP_LOGCONFIG(TAG, "Setting up max4820");
  this->spi_setup();
}

void MAX4820::dump_config() {
  ESP_LOGCONFIG(TAG, "MAX4820:");
  LOG_PIN("  CS Pin:", this->cs_);
}

bool MAX4820::get_switch_state(uint8_t switch_id);
void MAX4820::set_switch_state(uint8_t switch_id, bool state);

}  // namespace max4820
}  // namespace esphome
