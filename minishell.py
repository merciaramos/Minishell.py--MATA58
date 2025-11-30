import os
import subprocess
import locale

BUF_SIZE = 1024
ENC = locale.getpreferredencoding(False)  

def read_line():
    """Lê bytes da stdin usando os.read e retorna string sem newline"""
    try:
        data = os.read(0, BUF_SIZE)
        if not data:
            return None  # EOF
        s = data.decode(errors='ignore')
        if s.endswith('\n'):
            s = s[:-1]
        return s
    except OSError as e:
        os.write(2, f"Erro ao ler entrada: {e}\n".encode(ENC, errors="replace"))
        return ""

def parse_line(line):
    """Split simples em espaços/tabs, retorna lista de args (ou [] se vazio)"""
    if not line:
        return []
    return line.split()

def comando_nao_encontrado(cmd):
    """Mensagem personalizada (estilo Windows)."""
    msg = (
        f"{cmd} : O termo '{cmd}' não é reconhecido como como um comando interno ou externo, um programa operável ou um arquivo em lotes. "
    )
    os.write(2, msg.encode(ENC, errors="replace"))

def execute_command(args):
    """
    Tenta primeiro executar args como lista (programa externo).
    Se falhar (FileNotFoundError / OSError), tenta executar via shell (fallback),
    o que permite comandos internos como 'dir' e 'type' funcionarem.
    """
    if not args:
        return

    command_str = " ".join(args)

    try:

        # subprocess.Popen(args) no Windows vai funcionar como fork() + execvp()
        # cria um processo filho e executa o comando no mesmo passo
        proc = subprocess.Popen(args)

        # proc.wait() equivale ao wait() do processo pai = aguardando o fim do filho
        proc.wait()
        return

    except FileNotFoundError:
        pass
    except OSError:
        pass
    except Exception as e:

        # outros erros inesperados
        os.write(2, f"Erro ao executar '{args[0]}': {e}\n".encode(ENC, errors="replace"))
        return

    # fallback: executar via shell (aceita builtins do cmd/powershell)
    try:
        # usando shell=True com uma string. No Win o shell será o cmd por default
        proc = subprocess.Popen(command_str, shell=True)
        proc.wait()
    except FileNotFoundError:
        comando_nao_encontrado(args[0])
    except Exception as e:
        os.write(2, f"Erro ao executar via shell '{command_str}': {e}\n".encode(ENC, errors="replace"))


def main():
    while True:
        os.write(1, "> ".encode(ENC))
        line = read_line()
        if line is None:
            os.write(1, "\n".encode(ENC))
            break
        line = line.strip()
        if not line:
            continue
        args = parse_line(line)
        if not args:
            continue
        if args[0].lower() == "exit":
            break
        execute_command(args)

if __name__ == "__main__":
    main()
