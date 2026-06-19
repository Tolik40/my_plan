# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: ClientNotes
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
import sys

console = Console()

def show_menu():
    table = Table(title="Меню ClientNotes", style="cyan")
    table.add_column("ID", justify="center", width=5)
    table.add_column("Действие", style="bold")
    actions = [
        ("1", "Создать/Просмотреть заметку"),
        ("2", "Управление контактами"),
        ("3", "Запись встречи"),
        ("4", "Список задач"),
        ("5", "История решений"),
        ("0", "Выход")
    ]
    for idx, (id_, action) in enumerate(actions):
        table.add_row(id_, action)
    console.print(table)

def handle_choice(choice: str, data_store: dict):
    if choice == "1":
        note_id = Prompt.ask("ID заметки или Enter для новой", default="")
        if not note_id:
            title = Prompt.ask("Заголовок заметки")
            content = Prompt.ask("Текст заметки")
            data_store["notes"].append({"id": len(data_store["notes"]) + 1, "title": title, "content": content})
            console.print(Panel(f"Заметка #{len(data_store['notes'])} создана", style="green"))
        else:
            notes = data_store.get("notes", [])
            if notes and int(note_id) <= len(notes):
                n = notes[int(note_id)-1]
                console.print(Panel(f"ID: {n['id']}\n{title}: {n['content']}", title=f"Заметка #{n['id']}", border_style="blue"))
            else:
                console.print("[red]Заметка не найдена[/red]")
    elif choice == "2":
        contacts = data_store.get("contacts", [])
        if not contacts:
            console.print("[yellow]Список контактов пуст[/yellow]")
        else:
            c_table = Table(title="Контакты")
            c_table.add_column("ID")
            c_table.add_column("Имя")
            c_table.add_column("Телефон")
            for i, c in enumerate(contacts):
                c_table.add_row(str(i+1), c.get("name", ""), str(c.get("phone", "")))
            console.print(c_table)
    elif choice == "3":
        meet_id = Prompt.ask("ID встречи или Enter для новой")
        if not meet_id:
            title = Prompt.ask("Тема встречи")
            date = Prompt.ask("Дата (YYYY-MM-DD)")
            notes = data_store.setdefault("meetings", [])
            new_meet = {"id": len(notes) + 1, "title": title, "date": date}
            notes.append(new_meet)
            console.print(Panel(f"Встреча #{new_meet['id']} запланирована на {date}", style="green"))
        else:
            meetings = data_store.get("meetings", [])
