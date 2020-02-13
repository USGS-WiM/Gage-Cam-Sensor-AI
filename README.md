![WiM](wimlogo.png)


# Gage Cam Sensor AI

(This is a component of the larger Gage Cam Project)

The Sensor AI is a component developed for the remote sensor deployment of a pre-trained Keras deep learning model. This model was trained using the HPC Sensor AI component. 




### Prerequisites

Prerequisits are still under development and will appear here and in a make file once a final platform is established. At present, Sensor AI runs on Raspberry Pi 4, Raspberry Pi 3B, and AWS t2.micro w/ Ubuntu 16. Testing continues on Raspberry Pi 3 A+, Raspberry Pi Zero, Sparkfun Artemis Redboard, and Sparkfun Artemis Nano.

#### Raspberry Pi 3 A+ 
The sensor build requires the following components:

With sudo apt install:
- python >= 3.6
- libatlas-base-dev
With sud apt-get install python3-: 
- pip3 >= 20.0
- numpy
- scipy
- opencv
With pip3 install:
- wrapt (must be upgraded with the following code: pip3 install wrapt --upgrade --ignore-installed)
- h5py
- tensorflow
- keras


## Getting Started

This project is under development. Check the project engineering notebook to see project history and current efforts.

### Installing

To be announced after the current development phase is completed.

1. As supper user, alter the swap space in the file  /etc/dphys-swapfile from 100 to 4096

2. Restart swap with command  sudo /etc/init.d/dphys-swapfile restart

3. Run bash build.sh

4. Set swap back to 100 in /etc/dphys-swapfile

5. Restart swap with command  sudo /etc/init.d/dphys-swapfile restart

6. Reboot with command sudo reboot now

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
