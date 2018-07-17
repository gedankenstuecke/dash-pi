#!/usr/bin/env python

from phue import Bridge


def check_any_light_on(bridge):
    """
    Checks whether any lights on a given bridge are
    turned on. Returns True if yes, otherwise False
    """
    for i,group in bridge.get_group().items():
        if group['state']['any_on']:
            return True
    return False


def turn_off_lights(bridge):
    """
    Turn off all the lights of a
    bridge
    """
    for group_id in bridge.get_group():
        bridge.set_group(int(group_id), 'on', False)


def turn_on_lights(bridge):
    """
    Turn on all lights of the bridge.
    Default all lights to warm temperature,
    full brightness
    """
    for light in bridge.lights:
        bridge.set_light(light.light_id, {'ct': 350, 'bri': 254, 'on': True})


def toggle_lights(bridge):
    """
    If any light is on, turn all lights off.
    If all lights are off, turn all on.
    """
    if check_any_light_on(bridge):
        turn_off_lights(bridge)
    else:
        turn_on_lights(bridge)


def main():
    bridge = Bridge()
    toggle_lights(bridge)


if __name__ == "__main__":
    main()
