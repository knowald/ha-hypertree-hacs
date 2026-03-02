"""HA Hypertree — interactive tree visualizations for Home Assistant."""

from pathlib import Path

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.components import frontend

DOMAIN = "ha_hypertree"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    panel_dir = Path(__file__).parent
    panel_path = str(panel_dir / "hypertree.js")

    hass.http.register_static_path(
        f"/{DOMAIN}/hypertree.js", panel_path, cache_headers=False
    )

    frontend.async_register_built_in_panel(
        hass,
        "custom",
        sidebar_title="Hypertree",
        sidebar_icon="mdi:graph",
        frontend_url_path="hypertree",
        config={
            "_panel_custom": {
                "name": "ha-panel-hypertree",
                "js_url": f"/{DOMAIN}/hypertree.js",
                "embed_iframe": False,
            }
        },
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    frontend.async_remove_panel(hass, "hypertree")
    return True
