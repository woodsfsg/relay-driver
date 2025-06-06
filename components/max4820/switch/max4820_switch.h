#pragma once

#include "esphome/core/component.h"
#include "esphome/components/max4820/max4820.h"
#include "esphome/components/switch/switch.h"

namespace esphome {
namespace max4820 {

class MAX4820Switch : public switch_::Switch, public Component {
 public:
  void setup() override;
  void dump_config() override;
  void set_switch_output(uint8_t switch_output) { this->switch_output_ = switch_output; }

  void set_max4820_parent(MAX4820 *parent) { this->parent_ = parent; }

 protected:
  void write_state(bool state) override;

  MAX4820 *parent_;
  uint8_t switch_output_{0};
};

}  // namespace max4820
}  // namespace esphome
