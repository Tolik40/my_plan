# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: ClientNotes
def print_table(rows, headers):
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if len(str(cell)) > col_widths[i]:
                col_widths[i] = len(str(cell))
    lines = []
    sep_parts = ['-' * w for w in col_widths]
    header_line = '| ' + ' | '.join(sep_parts) + ' |'
    lines.append(header_line)
    lines.append('| ' + ' | '.join(sep_parts) + ' |')
    for row in rows:
        line = '| ' + ' | '.join(str(c).ljust(col_widths[i]) for i, c in enumerate(row)) + ' |'
        lines.append(line)
    last_line = '| ' + ' | '.join(sep_parts) + ' |'
    lines.append(last_line)
    print('\n'.join(lines))
