import subprocess
import threading

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing command: {command}")
        print(stderr.decode("utf-8"))
    else:
        print(stdout.decode("utf-8"))

def start_covenant():
    run_command("cd Covenant/Covenant && dotnet run")

def start_caldera():
    run_command("cd caldera && source .venv/bin/activate && python server.py --insecure")

def main():
    # Clonar repositório do C2 Covenant
    run_command("git clone https://github.com/cobbr/Covenant.git")

    # Acessar diretório do Covenant e instalar dependências
    run_command("cd Covenant && dotnet build")

    # Clonar repositório do Caldera
    run_command("git clone https://github.com/mitre/caldera.git --recursive --branch 2.9.0")

    # Acessar diretório do Caldera e instalar dependências
    run_command("cd caldera && python3 -m venv .venv && source .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt")

    # Iniciar o servidor do Covenant em uma thread separada
    covenant_thread = threading.Thread(target=start_covenant)
    covenant_thread.start()

    # Iniciar o servidor do Caldera em uma thread separada
    caldera_thread = threading.Thread(target=start_caldera)
    caldera_thread.start()

    # Aguardar as threads terminarem
    covenant_thread.join()
    caldera_thread.join()

if __name__ == "__main__":
    main()
