from esphome import pins
import esphome.codegen as cg
from esphome.components import spi
import esphome.config_validation as cv
from esphome.const import (
    CONF_CLOCK_PIN,
    CONF_DATA_PIN,
    CONF_ID,
    CONF_INVERTED,
    CONF_NUMBER,
    CONF_OUTPUT,
)

MULTI_CONF = True

max4820_ns = cg.esphome_ns.namespace("max4820")

MAX4820Component = max4820_ns.class_("MAX4820Component", spi.SPIDevice, cg.Component)

CONF_MAX4820 = "max4820"
CONF_SET_PIN = "set_pin"
CONF_RESET_PIN = "reset_pin"
CONF_SR_COUNT = "sr_count"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.Optional(CONF_SET_PIN): pins.gpio_output_pin_schema,
        cv.Optional(CONF_RESET_PIN): pins.gpio_output_pin_schema,
        cv.Optional(CONF_SR_COUNT, default=1): cv.int_range(min=1, max=4),
    }
).extend(cv.COMPONENT_SCHEMA).extend(spi.spi_device_schema(cs_pin_required=True)),


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await spi.register_spi_device(var, config)

    cg.add(var.set_sr_count(config[CONF_SR_COUNT]))
    cg.add(var.set_set_pin(config[CONF_SET_PIN]))
    cg.add(var.set_reset_pin(config[CONF_RESET_PIN]))
