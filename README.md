# Minishell - MATA 58 - Sistemas Operacionais


<h1 align="center"> MiniShell em Python </h1>

Um interpretador de comandos simples, escrito em Python, inspirado no comportamento de terminais reais como CMD e PowerShell.
O projeto demonstra conceitos fundamentais de parsing, execução de processos, tratamento de erros, modularização e loop de REPL (Read–Eval–Print Loop).

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=DESENVOLVIDO&color=GREEN&style=for-the-badge)
![GitHub Org's stars](https://img.shields.io/github/stars/camilafernanda?style=social)

# 🛠 Tecnologias Utilizadas

- Python 3.10+

- subprocess

- os


# :hammer: Funcionalidades do projeto

✔️ Execução de comandos nativos do sistema

✔️ Parsing básico de entrada do usuário

✔️ Tratamento customizado para comandos inválidos

✔️ Função personalizada comando_nao_encontrado() (mensagem estilo Windows)

✔️ Modularização:
- Leitura e parsing
- Execução
- Loop principal

✔️ Comando interno exit para encerrar o shell

✔️ Compatível com Windows, Linux e macOS

 # 🧠 Principais Componentes

🔹 comando_nao_encontrado(cmd)

🔹 parse_input()

🔹 executar_comando()

🔹 Loop REPL

# ⏯️ Como Executar

1. Clone o repositório
   - git clone https://github.com/merciaramos/Minishell.py--MATA58.git
  
2. Acesse o diretório
   - cd minishell.py

3. Execute
   -  python .\minishell.py

# 📄 Exemplos de comandos

> dir

> echo hello world

> ping google.com

> dffdffd        ← comando inválido

> exit           ← encerra o shell
