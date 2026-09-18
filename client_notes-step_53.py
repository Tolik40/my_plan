# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: ClientNotes
def export_records_as_text(records, field_names):
    """Write a list of records to a plain text file, one per line.

    Each line is a pipe-separated string of the given field names.
    Records must be ordered lists or dicts; dicts are converted via
    record.get(name) for each name.
    """
    if records and not isinstance(records[0], (list, dict)):
        raise TypeError("records must be a list of lists or dicts")

    with open("client_notes_export.txt", "w", encoding="utf-8") as f:
        for record in records:
            if isinstance(record, dict):
                line = " | ".join(str(record.get(name, "")) for name in field_names)
            else:
                line = " | ".join(str(record[i]) for i in range(len(field_names)))
            f.write(line + "\n")
