sudo apt-get install python-pip python-pip3
sudo pip install subprocess32
sudo pip install amazon-dash
sudo python -m amazon_dash.install

sudo cp amazon-dash.yml /etc/amazon-dash.yml

pip3 install phue

sudo systemctl start amazon-dash
sudo systemctl enable amazon-dash
