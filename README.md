![WiM](wimlogo.png)


# Gage Cam Sensor AI

(This is a component of the larger Gage Cam Project)

The Sensor AI is a component developed for the remote sensor deployment of a pre-trained Keras deep learning model. This model was trained using the HPC Sensor AI component. 

### Prerequisites

Pre-requisits are still under development and will appear here and in a make file once a final platform is established. At present, Sensor AI runs on Raspberry Pi 4, Raspberry Pi 3B, and AWS t2.micro w/ Ubuntu 16. Testing continues on Raspberry Pi 3 A+, Raspberry Pi Zero, Sparkfun Artemis Redboard, and Sparkfun Artemis Nano.

### Hardware
  - Raspberry Pi 3 A+
  - Raspberry Pi NoIR Camera v2.1
  - Witty Pi 3
  - Verizon USB Cellular Modem
  - microSD card  
  - Voltaic 12,800maH battery

### Install raspbian

Follow steps from raspbian installation guide [here](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)

- Flash image to microSD card using Balena Etcher
- Insert microSD card into pi and plug in

#### Set static IP on raspberry pi
Edit the dhcpcd conf: `sudo nano /etc/dhcpcd.conf`

Add or uncomment the following:

```bash
interface eth0
static ip_address=166.252.48.111/24
static routers=166.252.48.112
static domain_name_servers=166.252.48.112
```

### Configure raspbian

Once the pi has booted, log in using: user `pi` password `raspberry`

Run `sudo raspi-config` to run raspberry pi config wizard:

- change user password
- enable SSH
- enable camera
- change locale (en_US.UTF-8)
- change keyboard layout (generic 105 key US)

### Disable unneeded features for battery consumption

**Could do more research here**

Edit `sudo nano /boot/config.txt` then add the following:

```bash
#disable bluetooth
dtoverlay=pi3-disable-bt

#disable wifi
dtoverlay=pi3-disable-wifi

#disable onboard LED
dtparam=act_led_trigger=none
dtparam=act_led_activelow=on
```

### Install Software
Get install script and run using 'source':

```bash
wget https://raw.githubusercontent.com/USGS-WiM/Gage-Cam-Sensor-AI/dev/build.sh
source build.sh
```

### Set capture script to run on startup (this will then trigger AI model run)

Edit file  `sudo nano /etc/rc.local` and add the following after `fi` and before `exit 0:`

```bash
/usr/bin/python3 /home/pi/Gage-Cam-Sensor-AI/camera/capture.py

```

### WittyPi setup info

#### WittyPi Mini
Install wittyPi software: 

```bash
wget http://www.uugear.com/repo/WittyPi2/installWittyPi.sh
sudo sh installWittyPi.sh
```

#### WittyPi3
Install wittyPi software: 

```bash
wget http://www.uugear.com/repo/WittyPi3/install.sh
Run setup script: `sudo sh install.sh
```

#### WItty Pi create script to run every hour
create new schedule script to turn on 5 mins every hour.  In `/home/pi/wittyPi/schedules`:

```bash
cp on_5m_every_20m.wpi on_5m_every_60m.wpi
nano on_5m_every_60m.wpi
```

- change `OFF  M515` to `OFF M55`
- save and exit
- Open wittyPi setup script: `sudo sh ./wittyPi.sh` and select your new schedule script


## Building and testing

Run command python3 run_lite.py

## Deployment

Comming Soon...

## Built With

* [Python](https://python.org/) - The main web framework used
* [Keras](https://keras.io/) - Core model platform 
* [NPM](https://tensorflow.org/) - Core AI platform
* [Opencv](https://www.opencv.org/) - Preprocessing dependency

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on the process for submitting pull requests to us. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on adhering by the [USGS Code of Scientific Conduct](https://www2.usgs.gov/fsp/fsp_code_of_scientific_conduct.asp).

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](../../tags). 

Advance the version when adding features, fixing bugs or making minor enhancement. Follow semver principles. To add tag in git, type git tag v{major}.{minor}.{patch}. Example: git tag v2.0.5

To push tags to remote origin: `git push origin --tags`

*Note that your alias for the remote origin may differ.

## Authors

* **[Daniel Beckman](PROFILE_PAGE_URL_HERE)**  - *AI Developer* - [USGS Web Informatics & Mapping](https://wim.usgs.gov/)

See also the list of [contributors](../../graphs/contributors) who participated in this project.

## License

This project is licensed under the Creative Commons CC0 1.0 Universal License - see the [LICENSE.md](LICENSE.md) file for details

## Suggested Citation
In the spirit of open source, please cite any re-use of the source code stored in this repository. Below is the suggested citation:

`This project contains code produced by the Web Informatics and Mapping (WIM) team at the United States Geological Survey (USGS). As a work of the United States Government, this project is in the public domain within the United States. https://wim.usgs.gov`


## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration Note 

## About WIM
* This project authored by the [USGS WIM team](https://wim.usgs.gov)
* WIM is a team of developers and technologists who build and manage tools, software, web services, and databases to support USGS science and other federal government cooperators.
* WIM is a part of the [Upper Midwest Water Science Center](https://www.usgs.gov/centers/wisconsin-water-science-center).
