
# 🏥 Sistema de Cadastro de Pacientes – Clínica Saúde & Bem-Estar

Este é um aplicativo desktop desenvolvido em Python com interface gráfica em Tkinter e banco de dados SQLite. O sistema permite o cadastro, edição, exclusão e visualização de pacientes, com cálculo automático do IMC (Índice de Massa Corporal).

---

## 📌 Funcionalidades

- Cadastro de pacientes com nome, idade, peso e altura  
- Cálculo automático do IMC  
- Exibição dos pacientes em tabela interativa  
- Edição e exclusão de registros  
- Interface gráfica simples e funcional  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **SQLite3** – Banco de dados local
- **Tkinter** – Interface gráfica nativa do Python
- **Treeview (ttk)** – Exibição de dados em formato de tabela

---

## 🖼️ Interface do Sistema

![image](https://github.com/user-attachments/assets/7934aa6a-6be8-4e85-aa11-c459a9b4cbe2)


---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/projeto-clinica.git
```

2. **Acesse o diretório do projeto:**

```bash
cd projeto-clinica
```

3. **Execute o arquivo principal:**

```bash
python nome_do_arquivo.py
```

---

## 🧮 Cálculo do IMC

O sistema calcula automaticamente o IMC utilizando a fórmula:

```
IMC = peso / (altura²)
```

Esse valor é armazenado junto com os dados do paciente no banco de dados.

---

## 📂 Estrutura do Projeto

```
projeto-clinica/
├── clinica.db                # Banco de dados SQLite
├── main.py                   # Código-fonte principal
├── README.md                 # Documento descritivo
```

---

## 💡 Possíveis Melhorias Futuras

- Adicionar sistema de login para segurança
- Exportar dados para PDF/Excel
- Filtros de busca por nome ou IMC
- Validação visual com cores para níveis de IMC

---

## 📍 Aplicações Reais

- Clínicas de nutrição
- Consultórios de clínica geral
- Hospitais e postos de triagem
- Instituições de ensino (exercícios práticos em aulas de programação)

---

## 👨‍💻 Autor

Desenvolvido por Miguel Reis Ribeiro de Almeida  – estudante de programação 

---
