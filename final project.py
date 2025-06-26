
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def conectar():
    conn = sqlite3.connect('clinica.db')
    return conn
def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
       CREATE TABLE IF NOT EXISTS pacientes(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nome TEXT NOT NULL,
       idade INTEGER NOT NULL,
       peso REAL NOT NULL,
       altura REAL NOT NULL,
       imc REAL
       ) 
''')
    conn.commit()
    conn.close()
# CREATE CRIAR
def inserir_paciente():
    nome= entry_nome.get()
    idade = entry_idade.get()
    peso= entry_peso.get()
    altura = entry_altura.get()
    if nome and idade and peso and altura:
        try:
            idade = int(idade)
            peso = float(peso)
            altura = float(altura)
            imc = peso / (altura ** 2)
            conn = conectar()
            c = conn.cursor()
            c.execute('INSERT INTO pacientes(nome, idade, peso, altura, imc) VALUES(?,?,?,?,?)',
                      (nome, idade, peso, altura, imc))
            conn.commit()
            conn.close()
            messagebox.showinfo('dados inseridos com secesso')
            mostrar_pacientes()
        except ValueError:
            messagebox.showerror('ERRO', 'INSIRA VALORES VÁLIDOS')
    else:
        messagebox.showerror('ERRO', 'TODOS OS CAMPOS SÃO OBRIGATÓRIOS')
#read ler

def mostrar_pacientes():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM pacientes')
    pacientes = c.fetchall()
    for paciente in pacientes:
        tree.insert("", "end", values=(paciente[0], paciente[1], paciente[2], paciente[3], paciente[4], paciente[5]))
    conn.close()
#del
def del_paciente():
    dados_del=tree.selection()
    if dados_del:
        paciente_id = tree.item(dados_del)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM pacientes WHERE id = ?', (paciente_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'PACIENTE DELETADO COM SUCESSO')
        mostrar_pacientes()
    else:
        messagebox.showerror('ERRO', 'SELECIONE UM PACIENTE PARA DELETAR')
# update
def editar():
    seleção = tree.selection()
    if seleção:
        paciente_id=tree.item(seleção)['values'][0]
        novo_nome = entry_nome.get()
        nova_idade = entry_idade.get()
        novo_peso = entry_peso.get()
        nova_altura = entry_altura.get()
        if novo_nome and nova_idade and novo_peso and nova_altura:
            try:
                nova_idade = int(nova_idade)
                novo_peso = float(novo_peso)
                nova_altura = float(nova_altura)
                novo_imc = novo_peso / (novo_peso and novo_peso > 0 and novo_peso or 1) if novo_peso and novo_peso > 0 else 0
                novo_imc = novo_peso / (nova_altura ** 2)
                conn= conectar()
                c = conn.cursor()
                c.execute('UPDATE pacientes SET nome = ?, idade = ?, peso = ?, altura = ?, imc = ? WHERE id = ?', (novo_nome, nova_idade, novo_peso, nova_altura, novo_imc, paciente_id))
                conn.commit()
                conn.close()    
                messagebox.showinfo('EDIÇÃO', 'DADOS DO PACIENTE EDITADOS COM SUCESSO')
                mostrar_pacientes()
            except ValueError:
                messagebox.showerror('ERRO', 'INSIRA VALORES VÁLIDOS')
        else:
            messagebox.showerror('ERRO', 'TODOS OS CAMPOS SÃO OBRIGATÓRIOS')
    else:
        messagebox.showwarning('', 'SELECIONE UM PACIENTE PARA EDITAR')

janela = tk.Tk()
janela.configure(bg="#FFFFFF")
janela.title("Cadastro de Pacientes - Saúde & Bem-Estar")
janela.geometry("800x600")

titulo = tk.Label(janela, text="Cadastro de Pacientes", font=("Arial", 20), bg="#FFFFFF")
titulo.grid(row=0, column=0, columnspan=4, pady=10)
#---------------------------------------------------------------------------------
label_nome = tk.Label(janela, text="Nome:", bg="#FFFFFF")
label_nome.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=1, column=1, padx=10, pady=5)
#---------------------------------------------------------------------------------
label_idade = tk.Label(janela, text="Idade:", bg="#FFFFFF")
label_idade.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_idade = tk.Entry(janela, width=30)
entry_idade.grid(row=2, column=1, padx=10, pady=5)
#---------------------------------------------------------------------------------
label_peso = tk.Label(janela, text="Peso (kg):", bg="#FFFFFF")
label_peso.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_peso = tk.Entry(janela, width=30)
entry_peso.grid(row=3, column=1, padx=10, pady=5)
#---------------------------------------------------------------------------------
label_altura = tk.Label(janela, text="Altura (m):", bg="#FFFFFF")
label_altura.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_altura = tk.Entry(janela, width=30)
entry_altura.grid(row=4, column=1, padx=10, pady=5)
#---------------------------------------------------------------------------------
botao_inserir = tk.Button(janela, text="Cadastrar Paciente", command=inserir_paciente, bg="#000000", fg="#471616", font=("Arial", 12))
botao_inserir.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
botao_exibir = tk.Button(janela, text="Exibir Pacientes", command=mostrar_pacientes, bg="#000000", fg="#471616", font=("Arial", 12))
botao_exibir.grid(row=5, column=2, columnspan=2, padx=10, pady=10)
botao_deletar = tk.Button(janela, text="Deletar Paciente", command=del_paciente, bg="#000000", fg="#471616", font=("Arial", 12))
botao_deletar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
botao_editar = tk.Button(janela, text="Editar Paciente", command=editar, bg="#000000", fg="#471616", font=("Arial", 12))
botao_editar.grid(row=6, column=2, columnspan=2, padx=10, pady=10)
#---------------------------------------------------------------------------------
tree = ttk.Treeview(janela, columns=("ID", "Nome", "Idade", "Peso", "Altura", "IMC"), show='headings')
tree.grid(row=7, column=0, columnspan=4, padx=10, pady=10)

for col in tree["columns"]:
    tree.column(col, anchor="center", width=100)
    tree.heading(col, text=col)
criar_tabela()
mostrar_pacientes()

janela.mainloop()

