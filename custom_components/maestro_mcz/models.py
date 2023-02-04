from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
)

from homeassistant.helpers.entity import EntityCategory
from homeassistant.const import TEMP_CELSIUS

GENERIC_SENSORS = {
    "state": ["Current State", None, "mdi:power", None, None, True, EntityCategory.DIAGNOSTIC],
    "temp_amb_install": ["Temperature", TEMP_CELSIUS, "mdi:thermometer", SensorDeviceClass.TEMPERATURE, SensorStateClass.MEASUREMENT, True, None],
    "mode": ["Current Mode", None, "mdi:calendar-multiselect", None, None, True, EntityCategory.DIAGNOSTIC],
    "temp_fumi": ["Exhaust Temperature", TEMP_CELSIUS, "mdi:thermometer", SensorDeviceClass.TEMPERATURE, SensorStateClass.MEASUREMENT, True, EntityCategory.DIAGNOSTIC],
    "temp_scheda": ["Board Temperature", TEMP_CELSIUS, "mdi:thermometer", SensorDeviceClass.TEMPERATURE, SensorStateClass.MEASUREMENT, True, EntityCategory.DIAGNOSTIC],
    "mode": ["Current Mode", None, "mdi:calendar-multiselect", None, None, True, EntityCategory.DIAGNOSTIC],
    "vel_real_ventola_fumi": ["Exhaust Fan Speed", "rpm", "mdi:fan-chevron-up", None, SensorStateClass.MEASUREMENT, True, EntityCategory.DIAGNOSTIC],
    "vel_real_coclea": ["Transport Screw Speed", "rpm", "mdi:screw-lag", None, None, SensorStateClass.MEASUREMENT, EntityCategory.DIAGNOSTIC],
}

GENERIC_FANS = {
    # "set_vent_v1": ["Fan 1", "mdi:fan", {"0", "1", "2", "3", "4", "5", "6"}, 1, "Fan", True, EntityCategory.CONFIG]
}

models = {
    "CUTHDE08": {
        "sensor": {
            **GENERIC_SENSORS,
            **{
                # "temp_amb_install": ["Temperature", TEMP_CELSIUS, "mdi:thermometer", SensorDeviceClass.TEMPERATURE, SensorStateClass.MEASUREMENT, True, None],
            }
        },
        "fan": {
            **GENERIC_FANS,
            **{
                # "set_vent_v1": ["Fan 1", ["0", "1", "2", "3", "4", "5", "6"], 1, "Fan"]
            }
        },
        "switch": {
            **{
                "crono_enabled": ["Chrono", "mdi:timer", True, EntityCategory.CONFIG, "EnableChrono", "DisableChrono"],
                "att_eco": ["Start / Stop", "mdi:timer", True, EntityCategory.CONFIG, "EnableSS", "DisableSS"],
            }
        },
        "select": {
            **{
                "set_pot_man": ["Pot", "mdi:pot", True, EntityCategory.CONFIG, ["1", "2", "3", "4", "5"], "Pot"],
                "set_vent_v1": ["Fan 1", "mdi:fan", True, EntityCategory.CONFIG, ["0", "1", "2", "3", "4", "5", "6"], "Fan"],
            }
        },
        "binary_sensor": {
            **{
                "is_in_error": ["Error", "mdi:alert", True, EntityCategory.DIAGNOSTIC]
            }
        },
        "button": {
            **{
                "reset_alarm": ["Error Reset", "mdi:alert", True, EntityCategory.DIAGNOSTIC, "ResetErrors"]
            }
        }
    },
    "SC12": {
        "sensor": {
            **GENERIC_SENSORS,
        },
        "fan": {
            **GENERIC_FANS,
        }
    },
}
