"""Platform for Sensor integration."""
from . import MczCoordinator, models

from homeassistant.components.button import (
    ButtonEntity,
)
from homeassistant.core import callback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
ENTITY = "button"


async def async_setup_entry(hass, entry, async_add_entities):
    stoveList = hass.data[DOMAIN][entry.entry_id]
    entities = []
    for stove in stoveList:
        stove:MczCoordinator = stove
        model = stove.maestroapi.State.nome_banca_dati_sel
        for (prop, attrs) in models.models[model][ENTITY].items():
            entities.append(MczEntity(stove, prop, attrs))

    async_add_entities(entities)


class MczEntity(CoordinatorEntity, ButtonEntity):

    _attr_has_entity_name = True

    def __init__(self, coordinator, prop, attrs):
        super().__init__(coordinator)
        [name, icon, enabled_by_default, category, func] = attrs
        self.coordinator:MczCoordinator = coordinator
        self._attr_name = name
        self._attr_unique_id = f"{self.coordinator._maestroapi.Status.sm_sn}-{prop}"
        self._attr_icon = icon
        self._prop = prop
        self._enabled_default = enabled_by_default
        self._category = category
        self._func = func

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator._maestroapi.Status.sm_sn)},
        )

    async def async_press(self) -> None:
        await getattr(self.coordinator._maestroapi, self._func)()

    @property
    def entity_registry_enabled_default(self) -> bool:
        return self._enabled_default

    @property
    def entity_category(self):
        return self._category

    @callback
    def _handle_coordinator_update(self) -> None:
        self.async_write_ha_state()
