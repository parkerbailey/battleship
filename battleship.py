import tkinter as tk
from tkinter import ttk
import string
import ttkbootstrap 


class Battleship(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Battleship")
        self.resizable(False, False)
        
        # board setup
        board = ttk.Frame(self, width=500, height=500)   # 50 px per cell → 10 × 10 board
        board.pack()
        board.grid_propagate(False)

        # grid setup
        for i in range(10):
            board.grid_rowconfigure(i + 1, weight=1, uniform="cell")
            board.grid_columnconfigure(i + 1, weight=1, uniform="cell")
        for r in range(10):
            ttk.Label(board, text=string.ascii_uppercase[r]).grid(row=r + 1, column=0, padx=2, pady=2)
        for c in range(10):
            ttk.Label(board, text=str(c + 1)).grid(row=0, column=c + 1, padx=2, pady=2)
        self.grid_vars = [[tk.BooleanVar() for _ in range(10)] for _ in range(10)]
        for r in range(10):
            for c in range(10):
                ttk.Checkbutton(
                    board,
                    variable=self.grid_vars[r][c],
                    style="secondary.Outline.Toolbutton"
                ).grid(row=r + 1, column=c + 1, sticky="nsew")

        # validate button
        validate = ttk.Button(board, text="Validate Board", command=self.validate_board)
        validate.grid(row=11, column=1, columnspan=10, sticky='ew')

    def validate_board(self):
        pass
            

if __name__ == "__main__":
    app = Battleship()
    app.mainloop()