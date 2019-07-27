# HomeAssistant - MelView

HomeAssistant component for mitsubishi air conditioner (MelView)

## Installing

- Clone this repo to <config_dir>/custom_components/melview/

Edit configuration.yaml and add below lines:

``` yaml
climate:
  - platform: melview
    email: MY_EMAIL@gmail.com
    password: MY_PASSWORD
    local: yes

logger:
  default: warn
  logs:
    custom_components.melview.climate: debug
    custon_components.melview.melview: debug
```

## License

This project is licensed under the WTF License
