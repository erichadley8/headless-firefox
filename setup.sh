apt update
apt -y upgrade
apt install python3-pip
apt install -y build-essential libssl-dev libffi-dev python3-dev
pip3 install -r requirements.txt
export PATH=$PATH:$PWD
