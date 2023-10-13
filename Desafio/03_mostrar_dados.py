import csv

# Função para obter os IDs dos funcionários a partir do arquivo CSV
def get_employee_ids_from_csv():
    employee_ids = []
    with open("ids_funcionarios.csv", "r") as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            employee_ids.append(int(linha["ID"]))
    return employee_ids

# Função para obter os dados dos funcionários a partir do arquivo TXT com base nos IDs
def get_employee_data(employee_id):
    with open("funcionarios.txt", "r", encoding='latin-1') as arquivo_txt:
        funcionarios = []
        funcionario = {}
        for linha in arquivo_txt:
            linha = linha.strip()
            if linha.startswith("ID:"):
                if funcionario:
                    funcionarios.append(funcionario)
                funcionario = {"ID": int(linha.split(": ")[1])}
            elif ':' in linha:
                chave, valor = linha.split(": ", 1)
                funcionario[chave] = valor
        if funcionario:
            funcionarios.append(funcionario)
        
        for f in funcionarios:
            if f['ID'] == employee_id:
                return f
    return None

# Obter os IDs dos funcionários a partir do arquivo CSV
employee_ids = get_employee_ids_from_csv()

# Obter os dados dos funcionários com base nos IDs e criar uma lista de dicionários
employees = []
for employee_id in employee_ids:
    employee_data = get_employee_data(employee_id)
    if employee_data:
        employees.append(employee_data)

# Mostrar os dados dos funcionários
for employee in employees:
    print("Dados do Funcionário:")
    for chave, valor in employee.items():
        print(f"{chave}: {valor}")
    print()
