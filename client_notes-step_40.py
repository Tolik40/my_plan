# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: ClientNotes
import argparse

def main():
    parser = argparse.ArgumentParser(description="ClientNotes CLI")
    sub = parser.add_subparsers(dest="command")

    # new
    p_new = sub.add_parser("new", help="Create new item")
    p_new.add_argument("--client", required=True)
    p_new.add_argument("--type", choices=["note","contact","meeting","task","decision"], required=True)
    p_new.add_argument("--title", required=True)
    p_new.add_argument("--body", default="")

    # show
    p_show = sub.add_parser("show", help="Show item")
    p_show.add_argument("--id", required=True)

    # list
    p_list = sub.add_parser("list", help="List items")
    p_list.add_argument("--type", choices=["note","contact","meeting","task","decision"])

    # done
    p_done = sub.add_parser("done", help="Mark task as done")
    p_done.add_argument("--id", required=True)

    # delete
    p_del = sub.add_parser("delete", help="Delete item")
    p_del.add_argument("--id", required=True)

    args = parser.parse_args()
    if args.command == "new":
        save_item(args.client, args.type, args.title, args.body)
    elif args.command == "show":
        print(show_item(args.id))
    elif args.command == "list":
        print(list_items(args.type))
    elif args.command == "done":
        update_item(args.id, {"done": True})
    elif args.command == "delete":
        delete_item(args.id)
    else:
        parser.print_help()

main()
