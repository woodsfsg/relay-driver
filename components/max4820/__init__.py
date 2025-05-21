import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import spi
from esphome.const import CONF_ID
from esphome import pins

DEPENDENCIES = ["spi"]
AUTO_LOAD = ["switch"]
MULTI_CONF = True

CONF_MAX3008 = "max4820"
CONF_RESET_PIN = "reset_pin"
CONF_SET_PIN = "set pin"
CONF_SR_NUM = "sr_num"

max4820_ns = cg.esphome_ns.namespace("max4820")
MAX4820 = max4820_ns.class_("MAX4820", cg.Component, spi.SPIDevice)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(MAX4820),
        cv.Optional(CONF_SET_PIN): pins.gpio_output_pin_schema,
        cv.Optional(CONF_RESET_PIN): pins.gpio_output_pin_schema,
        cv.Optional(CONF_SR_NUM, default=1): cv.int_range(min=1,max=4),
    }
).extend(spi.spi_device_schema(cs_pin_required=True))


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await spi.register_spi_device(var, config)

    if CONF_RESET_PIN in config:
        reset_pin_ = await cg.gpio_pin_expression(config[CONF_RESET_PIN])
        cg.add(var.set_reset_pin(reset_pin_))
    if CONF_SET_PIN in config:
        set_pin_ = await cg.gpio_pin_expression(config[CONF_SET_PIN])
        cg.add(var.set_reset_pin(set_pin_))
    if CONF_SR_NUM in config:
        cg.add(var.set_sr_num(config[CONF_SR_NUM]))
