"""Constants for the MySmartBike integration."""
from __future__ import annotations

from datetime import timedelta
import logging

from homeassistant.const import Platform

MYSMARTBIKE_PLATFORMS = [Platform.SENSOR, Platform.DEVICE_TRACKER]

DOMAIN = "mysmartbike"
LOGGER = logging.getLogger(__package__)
UPDATE_INTERVAL = timedelta(seconds=300)

USE_SIMULATOR = False
API_BASE_URI_CLOUD = "https://my-smartbike.com"
API_BASE_URI_SIMULATOR = "http://0.0.0.0:8001"
API_BASE_URI = API_BASE_URI_CLOUD if not USE_SIMULATOR else API_BASE_URI_SIMULATOR

USE_PROXY = False
DISABLE_SSL_CERT_CHECK = USE_PROXY
SYSTEM_PROXY: str | None = None if not USE_PROXY else "http://0.0.0.0:8080"
PROXIES: dict | None = {} if not USE_PROXY else {"https": SYSTEM_PROXY}

API_USER_AGENT = "ENDUSER/2.1.1 (com.mahle.sbs; build 9; IOS 17.3)"
API_X_APP = "ENDUSER"
API_X_PLATFORM = "IOS"
API_X_THEME = "DARK"
API_X_VERSION = "2.1.1"