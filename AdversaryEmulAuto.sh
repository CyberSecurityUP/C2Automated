#!/bin/bash

# Verifique se o script está sendo executado como root
if [[ $EUID -ne 0 ]]; then
   echo "Este script deve ser executado como root" 
   exit 1
fi

# Atualize o sistema
apt-get update && apt-get upgrade -y

# Instale as dependências necessárias
apt-get install -y git python3-pip

# Instale e execute o APT Simulator
git clone https://github.com/NextronSystems/APTSimulator.git
cd APTSimulator
chmod +x APTSimulator.sh
./APTSimulator.sh
cd ..

# Instale e execute o BloodHound
apt-get install -y bloodhound
bloodhound

# Instale e execute o Caldera
git clone https://github.com/mitre/caldera.git --recursive --branch 3.0.0
cd caldera
pip3 install -r requirements.txt
python3 server.py &
cd ..

# Instale e execute o Metta
git clone https://github.com/uber-common/metta.git
cd metta
pip3 install -r requirements.txt
python3 setup.py install
cd ..
metta-cli

# Instale e execute o Red Team Automation (RTA)
git clone https://github.com/endgameinc/RTA.git
cd RTA
pip3 install -r requirements.txt
python3 rta.py -h
cd ..

# Instale e execute o AutoTTP
git clone https://github.com/cr0hn/autottp.git
cd autottp
pip3 install -r requirements.txt
python3 autottp.py -h
cd ..

echo "Todas as ferramentas foram instaladas e executadas. Verifique a saída de cada ferramenta para garantir que estejam funcionando corretamente."
