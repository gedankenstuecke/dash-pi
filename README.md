# Using Amazon Dash buttons for controling Hue lights

Some simple scripts to use a Raspberry Pi Zero W (with Raspian Stretch Lite)
as backend to creatively re-use *Amazon Dash Buttons* as Hue light switches.

## The Raspberry Pi Setup
First steps: [Download a Raspian image](https://www.raspberrypi.org/downloads/raspbian/) and flash it onto a SD card [using Etcher or whatever](https://etcher.io/) other tool you prefer. The *Lite* image is enough as
the Pi will run headless.

### Enable Autoconnect to WiFi & SSH
(based on [this useful article](https://core-electronics.com.au/tutorials/raspberry-pi-zerow-headless-wifi-setup.html)).

- mount your flashed SD card on your computer (not the Raspberry Pi!), it will show up as `boot`
- in the root folder of the SD card create a file called `wpa_supplicant.conf`

Enter the following in the file, and adjust `ssid` and `psk` with your Wifi's name & passphrase:

```
country=us
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 scan_ssid=1
 ssid="MyNetworkSSID"
 psk="Pa55w0rd1234"
}
```

To also enable `ssh` access to the machine create an empty file called `ssh` in the root folder of the SD card.

### Boot the Pi & connect
Now you can slide your SD card into the Pi and power it up. Once it's booted you can SSH into it by using

```
ssh pi@raspberrypi.local
```

The standard password is `raspberry`. Once you're connected you should run

```
sudo raspi-config
```

and change things like the `hostname`, `password` etc. Also make sure that you permanently enable the `ssh` access here!


## Installing all dependencies
See `setup.sh`. You want to first install `pip`, `pip3`, `tcpdump`:

```
sudo apt-get install python-pip python-pip3 tcpdump
```

Now you can install `amazon-dash`, it's dependencies & the `service`:

```
sudo pip install subprocess32
pip3 install phue
sudo pip install amazon-dash
sudo python -m amazon_dash.install
```

## Setup Amazon Dash buttons & `amazon-dash`
With that out of the way we can set up our *Dash Buttons*. Use the *Amazon* app
for your phone to start the initial setup and get the buttons into your WiFi.

**Important** Only setup the connection to the WiFi, **don't** select the product they should buy!

Pressing the buttons now should lead to you getting a *failed order* notification on your phone. If these annoy you to much you can use your router's settings to ban the buttons from accessing the internet later on. A simple way for that is to
- first give them a fixed IP assignment based on their MAC address (see below to find it) and then banning all internet ports for that IP.

To find the MAC address of your buttons you can run

```
sudo amazon-dash discovery
```

on your Raspberry Pi. Once you press the button their MAC address will appear. Use this for setting up your router and/or the `amazon-dash.yml`. An example of the `amazon-dash.yml` is in this repository.

Once you've finished your `amazon-dash.yml` you can `scp` it onto the Raspberry Pi, make it owned by root (`chown root:root amazon-dash.yml`) and then move it to `/etc/amazon-dash.yml`.

You can now restart: the `amazon-dash` service:

```
sudo systemctl stop amazon-dash
sudo systemctl start amazon-dash
```

Use the following to make sure that the dash service starts when the Pi is rebooted:

```
sudo systemctl enable amazon-dash
```
