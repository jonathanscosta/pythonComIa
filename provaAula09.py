import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = "auto"

    
    tarefas = ft.Column()

    
    campo_tarefa = ft.TextField(label="Digite uma nova tarefa", expand=True)

    
    def adicionar_tarefa(e):
        if campo_tarefa.value.strip() != "":
            
            tarefas.controls.append(ft.Text(f"• {campo_tarefa.value}"))
            campo_tarefa.value = ""  
            page.update()  

    
    botao_adicionar = ft.ElevatedButton(text="Adicionar", on_click=adicionar_tarefa)

    
    page.add(
        ft.Row([campo_tarefa, botao_adicionar]),
        tarefas
    )


ft.app(target=main)
