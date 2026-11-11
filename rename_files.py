import os
import unicodedata
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


def remove_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return "".join(c for c in normalized if unicodedata.category(c) != "Mn")


def rename_files(directory: str, log: scrolledtext.ScrolledText) -> None:
    log.config(state="normal")
    log.delete("1.0", tk.END)

    if not os.path.isdir(directory):
        log.insert(tk.END, "Diretorio invalido.\n")
        log.config(state="disabled")
        return

    renamed = 0
    skipped = 0

    for filename in sorted(os.listdir(directory)):
        new_name = remove_accents(filename)
        if new_name == filename:
            skipped += 1
            continue

        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_name)

        if os.path.exists(dst):
            log.insert(tk.END, f"[CONFLITO] '{filename}' -> '{new_name}' ja existe, pulando.\n")
            skipped += 1
            continue

        os.rename(src, dst)
        log.insert(tk.END, f"[OK] '{filename}' -> '{new_name}'\n")
        renamed += 1

    log.insert(tk.END, f"\nConcluido: {renamed} renomeado(s), {skipped} sem alteracao.\n")
    log.config(state="disabled")


def browse_directory(entry: tk.Entry) -> None:
    path = filedialog.askdirectory(title="Selecionar pasta")
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)


def main() -> None:
    root = tk.Tk()
    root.title("Remover acentos dos nomes de arquivo")
    root.resizable(False, False)

    pad = {"padx": 10, "pady": 5}

    frame_top = tk.Frame(root)
    frame_top.pack(fill="x", **pad)

    tk.Label(frame_top, text="Pasta:").pack(side="left")

    entry_dir = tk.Entry(frame_top, width=50)
    entry_dir.pack(side="left", padx=(5, 5))

    tk.Button(
        frame_top,
        text="Procurar...",
        command=lambda: browse_directory(entry_dir),
    ).pack(side="left")

    log = scrolledtext.ScrolledText(root, width=70, height=20, state="disabled")
    log.pack(**pad)

    tk.Button(
        root,
        text="Renomear arquivos",
        bg="#2563eb",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        padx=10,
        pady=4,
        command=lambda: rename_files(entry_dir.get().strip(), log),
    ).pack(pady=(0, 10))

    root.mainloop()


if __name__ == "__main__":
    main()
