cd home
sudo apt-get update
sudo apt-get install -y python3 python3-pip git
sudo apt-get install python3-tk
git clone https://github.com/kaidrumm/csci5253-lab6.git lab6
cd lab6
sudo apt install -y protobuf-compiler
sudo pip3 install grpcio-tools flask jsonpickle pillow requests
export FLASK_APP=rest_server
nohup flask run -h 0.0.0.0 &