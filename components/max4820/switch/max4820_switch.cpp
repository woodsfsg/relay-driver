#include "esphome/core/log.h"
#include "max4820_switch.h"

namespace esphome {
namespace max4820 {

static const char *const TAG = "max4820.switch";

void MAX4820Switch::setup() {
  bool state = this->parent_->get_switch_state(this->switch_output_);
  this->publish_state(state);
}

void MAX4820Switch::write_state(bool state) {
  ESP_LOGD(TAG, "Setting switch %u: %s", this->switch_output_, ONOFF(state));
  this->parent_->set_switch_state(this->switch_output_, state);
  this->publish_state(state);
}

void MAX4820Switch::dump_config() {
  LOG_SWITCH("", "MAX4820 Switch", this);
  ESP_LOGCONFIG(TAG, "  Switch has ID %u", this->switch_output_);
}

}  // namespace max4820
}  // namespace esphome
