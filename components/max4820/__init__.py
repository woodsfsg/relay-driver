from esphome import pins
import esphome.codegen as cg
from esphome.components import spi
from esphome.components import switch
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

MAX4820Switch = max4820_ns.class_(
    "MAX4820Switch", cg.Switch, cg.Parented.template(MAX4820Component)
)

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


MAX4820_SWITCH_SCHEMA = switch.switch_schema(
    MAX4820Switch,
    block_inverted=False,
).extend(
    {
        cv.Required(CONF_MAX4820): cv.use_id(MAX4820Component),
        cv.Required(CONF_NUMBER, default=1): cv.int_range(min=0, max=31),
    }
)


def max4820_switch_final_validate(relay_config, parent_config):
    max_relay = parent_config[CONF_SR_COUNT] * 8
    if relay_config[CONF_NUMBER] >= max_switch:
        raise cv.Invalid(f"Relay number must be less than {max_relay}")


async def max4820_switch_to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_parented(var, config[CONF_MAX4820])

    cg.add(var.set_number(config[CONF_NUMBER]))
    cg.add(var.set_inverted(config[CONF_INVERTED]))
    return var
