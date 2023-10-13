import csv
import os

listaFuncionarios = []

def salvarFuncionariosTXT():
    with open("funcionarios.txt", "w") as arquivo_txt:
        for funcionario in listaFuncionarios:
            arquivo_txt.write(f"ID: {funcionario['ID']}\n")
            arquivo_txt.write(f"Nome: {funcionario['Nome']}\n")
            arquivo_txt.write(f"Setor: {funcionario['Setor']}\n")
            arquivo_txt.write(f"Carga Horária Semanal: {funcionario['Carga Horária Semanal']}\n")
            arquivo_txt.write(f"Salario: {funcionario['Salário']}\n")
            arquivo_txt.write("\n")

def salvarIDsCSV():
    with open("ids_funcionarios.csv", "w", newline="") as arquivo_csv:
        campo_id = ["ID"]
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campo_id)
        escritor.writeheader()
        for funcionario in listaFuncionarios:
            escritor.writerow({"ID": funcionario['ID']})

def carregarFuncionarios():
    try:
        with open("funcionarios.txt", "r") as arquivo:
            funcionarios = []
            funcionario = {}
            for linha in arquivo:
                linha = linha.strip()
                if linha.startswith("ID:"):
                    if funcionario:
                        funcionarios.append(funcionario)
                        funcionario = {}
                else:
                    if ':' in linha:
                        chave, valor = linha.split(": ", 1)
                        funcionario[chave] = valor
            if funcionario:
                funcionarios.append(funcionario)
            return funcionarios
    except FileNotFoundError:
        return []

def cadastroFuncionario():
    funcionario = {}
    
    dadoNome = input("Qual o nome do funcionário? ")
    funcionario['Nome'] = dadoNome
    
    dadoSetor = input("Setor: ")
    funcionario['Setor'] = dadoSetor
    
    try:
        dadoCargaHoraria = float(input("Carga Horária Semanal: "))
    except ValueError:
        print("Valor inválido para Carga Horária Semanal. Usando 0.0 como valor padrão.")
        dadoCargaHoraria = 0.00
    funcionario['Carga Horária Semanal'] = dadoCargaHoraria
    
    try:
        dadoSalario = float(input("Salário: "))
    except ValueError:
        print("Valor inválido para Salário. Usando 0.0 como valor padrão.")
        dadoSalario = 0.0
    funcionario['Salário'] = dadoSalario

    # Gere um ID para o funcionário
    if not listaFuncionarios:
        funcionario['ID'] = 1
    else:
        ultimo_id = listaFuncionarios[-1]['ID']
        funcionario['ID'] = ultimo_id + 1
        
    listaFuncionarios.append(funcionario)
    salvarFuncionariosTXT()
    salvarIDsCSV()
    print("Funcionário cadastrado com sucesso!")

def resumoFuncionario():
    print("Dados da lista de funcionários: ")
    for i, funcionario in enumerate(listaFuncionarios, start=1):
        print(f'ID: {funcionario["ID"]}, Nome: {funcionario["Nome"]}, Setor: {funcionario["Setor"]}, Carga Horária Semanal: {funcionario["Carga Horária Semanal"]}, Salário: {funcionario["Salário"]}')

listaFuncionarios = carregarFuncionarios()

def menu():
    print(" - - - - - - - - - MENU - - - - - - - - -")
    print(" | 1 - Cadastrar Funcionário            |")
    print(" | 2 - Resumo de Dados                  |")
    print(" | 3 - Sair                             |")
    print(" - - - - - - - - - - - - - - - - - - - -")
    print("--- Escolha uma opção ---\n")
    op = int(input())
    return op

while True:
    op = menu()
    if op == 1:
        cadastroFuncionario()
    elif op == 2:
        resumoFuncionario()
    elif op == 3:
        print("Saiu")
        break
    else:
        print("Opção inválida, tente novamente.")
