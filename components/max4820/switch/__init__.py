import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import switch
from esphome.const import (
  CONF_ID,
  CONF_NUMBER,
)

from .. import max4820_ns MAX4820

DEPENDENCIES = ["max4820"]

MAX4820Switch = max4820_ns.class_("MAX4820Switch", switch.Switch, cg.Component)
CONF_MAX4820_ID = "max4820_id"
CONF_SWITCH_OUTPUT = "output"

CONFIG_SCHEMA = (
  switch.switch_schema(MAX4820Switch)
  .extend(
      {
          cv.GenerateID(CONF_MAX4820_ID): cv.use_id(MAX4820),
          cv.Required(CONF_NUMBER): cv.int_range(min=0, max=7),
      }
  )
  .extend(cv.COMPONENT_SCHEMA)
)
