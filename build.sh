#The following scipt will build all neccisary libraries on the sensor device

sudo apt -y update
sudo apt -y full-upgrade
sudo apt-get install -y python3 --update
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-numpy
sudo apt-get install -y python3-scipy
sudo apt install -y libatlas-base-dev
sudo pip3 install -y wrapt --upgrade --ignore-installed
sudo pip3 install -y h5py
sudo pip3 install -y tensorflow
sudo pip3 install -y keras
sudo apt-get install -y python3-opencv