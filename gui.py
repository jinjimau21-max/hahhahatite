import tkinter as tk 
from tkinter import ttk, messagebox
from datetime import datetime
import math

Total_Spaces = 20 
Min_Hours = 1 

Rate = {
  "Car" = 30, 
  "Motorcycle" 20
} 
 OVERTIME_RATE = 10.0

FREE_COLOR = "#4caf50"  #means available
BUSY_COLOR = "#e53935"  #means not available 
SELECT_COLOR = "#1e88e5" #means selected

class ParkingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Parking Management System")
        self.geometry("900x560")
        self.resizable(False, False)

        # spaces: index -> None or dict(plate, type, entry)
        self.spaces = {i: None for i in range(1, TOTAL_SPACES + 1)}
        self.revenue = 0.0
        self.selected = None
        self.buttons = {}

        self.build_ui()
        self.refresh()
        self.tick()
