# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: ClientNotes
import unittest

class TestClientNotes(unittest.TestCase):
    def test_add_contact(self):
        app = ClientNotesApp()
        app.add_contact("Иван Иванов", "+79001234567")
        contacts = app.get_contacts()
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0]["name"], "Иван Иванов")
        self.assertEqual(contacts[0]["phone"], "+79001234567")
        self.assertEqual(contacts[0]["email"], "")

    def test_add_meeting(self):
        app = ClientNotesApp()
        app.add_contact("Петр Петров", "+79007654321")
        app.add_meeting("Петр Петров", "2026-05-20", "Обсуждение контракта", "10:00")
        meetings = app.get_meetings()
        self.assertEqual(len(meetings), 1)
        self.assertEqual(meetings[0]["client"], "Петр Петров")
        self.assertEqual(meetings[0]["date"], "2026-05-20")
        self.assertEqual(meetings[0]["topic"], "Обсуждение контракта")

    def test_add_task(self):
        app = ClientNotesApp()
        app.add_contact("Анна Сидорова", "+79001112233")
        app.add_task("Анна Сидорова", "Подготовить коммерческое предложение", "Высокий")
        tasks = app.get_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["client"], "Анна Сидорова")
        self.assertEqual(tasks[0]["text"], "Подготовить коммерческое предложение")
        self.assertEqual(tasks[0]["priority"], "Высокий")

    def test_add_solution_history(self):
        app = ClientNotesApp()
        app.add_contact("Сергей Кузнецов", "+79004445566")
        app.add_solution_history("Сергей Кузнецов", "Оффер отклонен, клиент ждет скидку 10%")
        solutions = app.get_solutions()
        self.assertEqual(len(solutions), 1)
        self.assertEqual(solutions[0]["client"], "Сергей Кузнецов")
        self.assertEqual(solutions[0]["text"], "Оффер отклонен, клиент ждет скидку 10%")

    def test_get_all_summary(self):
        app = ClientNotesApp()
        app.add_contact("Дмитрий Орлов", "+79007778899")
        app.add_meeting("Дмитрий Орлов", "2026-06-01", "Встреча в офисе", "14:00")
        app.add_task("Дмитрий Орлов", "Отправить договор", "Низкий")
        app.add_solution_history("Дмитрий Орлов", "Договор подписан")
        summary = app.get_summary()
        self.assertIn("Дмитрий Орлов", summary["contacts"])
        self.assertIn("Дмитрий Орлов", summary["meetings"])
        self.assertIn("Дмитрий Орлов", summary["tasks"])
        self.assertIn("Дмитрий Орлов", summary["solutions"])

if __name__ == "__main__":
    unittest.main()
