import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ADDRESS,
    CONF_HUMIDITY,
    CONF_ID,
    CONF_TEMPERATURE,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_TEMPERATURE,
    STATE_CLASS_MEASUREMENT,
    UNIT_CELSIUS,
    UNIT_PERCENT,
)

from esphome.components.remote_base import (
    RemoteReceiverBase,
    CONF_RECEIVER_ID,
    register_listener,
)

DEPENDENCIES = ["remote_receiver"]

tx141th_bv2_ns = cg.esphome_ns.namespace("tx141th_bv2")

TX141TH_BV2Component = tx141th_bv2_ns.class_("TX141TH_BV2", cg.Component)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(TX141TH_BV2Component),
        cv.Optional(CONF_TEMPERATURE): sensor.sensor_schema(
            unit_of_measurement=UNIT_CELSIUS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_TEMPERATURE,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_HUMIDITY): sensor.sensor_schema(
            unit_of_measurement=UNIT_PERCENT,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_HUMIDITY,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Required(CONF_ADDRESS): cv.hex_uint8_t,
    }
).extend(
    {
        cv.GenerateID(CONF_RECEIVER_ID): cv.use_id(RemoteReceiverBase),
    }
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    cg.add(var.set_address(config[CONF_ADDRESS]))
    await register_listener(var, config)

    if CONF_TEMPERATURE in config:
        conf = config[CONF_TEMPERATURE]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_temperature_sensor(sens))

    if CONF_HUMIDITY in config:
        conf = config[CONF_HUMIDITY]
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_humidity_sensor(sens))
