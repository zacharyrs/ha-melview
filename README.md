# HomeAssistant - MelView

HomeAssistant component for mitsubishi air conditioner (MelView)

## Alternatives with more functionality

Unfortunately, I've had very little time to focus on this, so it's stagnated with a few things to do.
Currently it lacks `async` support, plus zones and dynanamic fan speeds are only in the `dev` branch.

There is a fork - https://github.com/haggis663/ha-melview - which has this plus releases to HACS, so that's probably the best replacement for anyone who needs more functionality.

I do hope to work on this again in the future, but I have no idea when...

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

## Dev Branch

There is initial support for zones and dynamic fan speeds in https://github.com/zacharyrs/ha-melview/tree/dev.  
If you require those features, please test them out on that branch!

## License

This project is licensed under the WTF License
