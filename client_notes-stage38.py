# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: ClientNotes
def test_edge_cases():
    """Test error and boundary cases for ClientNotes."""
    from clientnotes import ClientNotes, Contact, Meeting, Task, Decision

    notes = ClientNotes()

    # Test duplicate contact creation
    contact1 = Contact("Ivan", "+79991112233", "ivan@example.com")
    contact2 = Contact("Ivan", "+79991112233", "ivan@example.com")
    notes.add_contact(contact1)
    notes.add_contact(contact2)
    assert len(notes.contacts) == 1

    # Test duplicate meeting for same client
    meeting1 = Meeting("Project Kickoff", "2024-01-15", "2024-01-17", "Project A", "Ivan", "Ivan")
    meeting2 = Meeting("Project Kickoff", "2024-01-15", "2024-01-17", "Project A", "Ivan", "Ivan")
    notes.add_meeting(meeting1)
    notes.add_meeting(meeting2)
    assert len(notes.meetings) == 1

    # Test duplicate task for same client
    task1 = Task("Update proposal", "2024-01-20", "2024-01-22", "Project A", "Ivan", "Ivan")
    task2 = Task("Update proposal", "2024-01-20", "2024-01-22", "Project A", "Ivan", "Ivan")
    notes.add_task(task1)
    notes.add_task(task2)
    assert len(notes.tasks) == 1

    # Test duplicate decision for same client
    decision1 = Decision("Choose framework", "Python", "2024-01-25", "Ivan", "Ivan")
    decision2 = Decision("Choose framework", "Python", "2024-01-25", "Ivan", "Ivan")
    notes.add_decision(decision1)
    notes.add_decision(decision2)
    assert len(notes.decisions) == 1

    # Test empty notes
    assert notes.contacts == []
    assert notes.meetings == []
    assert notes.tasks == []
    assert notes.decisions == []

    # Test get_contact with non-existent contact
    assert notes.get_contact("+79999999999") is None

    # Test get_meeting with non-existent meeting
    assert notes.get_meeting("2024-01-15", "Ivan", "Ivan") is None

    # Test get_task with non-existent task
    assert notes.get_task("2024-01-20", "Ivan", "Ivan") is None

    # Test get_decision with non-existent decision
    assert notes.get_decision("2024-01-25", "Ivan", "Ivan") is None

    print("All edge case tests passed!")
