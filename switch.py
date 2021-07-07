import logging
from .melview import MelViewAuthentication, MelView
from homeassistant.components.switch import SwitchEntity

_LOGGER = logging.getLogger(__name__)
DOMAIN = 'melview'
REQUIREMENTS = ['requests']
DEPENDENCIES = []

class MelViewZoneSwitch(SwitchEntity):
    """ Melview zone switch handler for HomeAssistants
    """
    def __init__(self, zone, parentClimate):
        self._id = zone.id
        self._name = zone.name
        self._status = zone.status
        self._climate = parentClimate

    def update(self):
        self._climate.force_update()
        zone = self._climate.get_zone(self._id)
        self._name = zone.name
        self._status = zone.status

    @property
    def name(self):
        """ Diplay name for HASS
        """
        return f"{self._name} AC Zone"

    @property
    def unique_id(self):
        """ Get unique_id for HASS
        """
        return f"{self._climate.get_id()}-{self._id}"

    @property
    def should_poll(self):
        """ Ensure HASS polls the zone
        """
        return True

    @property
    def is_on(self):
        """ Check zone is on
        """
        return self._status == 1

    def turn_on(self):
        """ Turn on the zone
        """
        _LOGGER.debug('power on zone')
        if self._climate.enable_zone(self._id):
            self._status = 1

    def turn_off(self):
        """ Turn off the zone
        """
        _LOGGER.debug('power off zone')
        if self._climate.disable_zone(self._id):
            self._status = 0


def setup_platform(hass, config, add_devices, discovery_info=None):
    """ Set up the HASS component
    """
    _LOGGER.debug('adding component')

    email = config.get('email')
    password = config.get('password')
    local = config.get('local')

    if email is None:
        _LOGGER.error('no email provided')
        return False

    if password is None:
        _LOGGER.error('no password provided')
        return False

    if local is None:
        _LOGGER.warning('local unspecified, defaulting to false')
        local = False

    mv_auth = MelViewAuthentication(email, password)
    if not mv_auth.login():
        _LOGGER.error('login combination')
        return False

    melview = MelView(mv_auth, localcontrol=local)

    device_list = []

    devices = melview.get_devices_list()
    for device in devices:
        for zone in device.get_zones():
            _LOGGER.debug('new device: %s', device.get_friendly_name())
            device_list.append(MelViewZoneSwitch(zone, device))

    add_devices(device_list)

    _LOGGER.debug('component successfully added')
    return True
