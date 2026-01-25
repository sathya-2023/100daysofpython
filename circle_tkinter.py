import tkinter as tk
import math

W, H = 600, 600
CX, CY = W // 2, H // 2

STOP = math.pi * 7.1

R1 = 50   # first radius
R2 = 50   # second radius

root = tk.Tk()
canvas = tk.Canvas(root, width=W, height=H, bg="black")
canvas.pack()

canvas.create_oval(CX-3, CY-3, CX+3, CY+3, fill="white", outline="")
n = 5
radius = 0.0
angle1 = 0.0
angle2 = 0.0

GROW_STEP = 2
A1_STEP = n * 0.02
A2_STEP = n * 0.02 * math.pi # faster second rotation

line1 = None
line2 = None
last_x2 = None
last_y2 = None

def animate():
    global radius, angle1, angle2, line1, line2, last_x2, last_y2

    if line1:
        canvas.delete(line1)
    if line2:
        canvas.delete(line2)

    # Phase 1: grow first radius
    if radius < R1:
        x1 = CX + radius
        y1 = CY
        line1 = canvas.create_line(CX, CY, x1, y1, fill="white", width=1)
        radius += GROW_STEP
        root.after(16, animate)
        return

    if angle1 < STOP:
        color = "white"
    else:
        color = "cyan"

    # Phase 2: rotate first radius
    if angle1 >= 2*STOP:
        return

    x1 = CX + R1 * math.cos(angle1)
    y1 = CY - R1 * math.sin(angle1)

    line1 = canvas.create_line(CX, CY, x1, y1, fill="gray", width=1)

    # Second radius from endpoint of first
    x2 = x1 + R2 * math.cos(angle2)
    y2 = y1 - R2 * math.sin(angle2)

    line2 = canvas.create_line(x1, y1, x2, y2, fill="white", width=1)

    # Trace only second endpoint
    if last_x2 is not None:
        canvas.create_line(last_x2, last_y2, x2, y2, fill=color, width=0.1)

    last_x2, last_y2 = x2, y2

    angle1 += A1_STEP
    angle2 += A2_STEP

    root.after(16, animate)

animate()
root.mainloop()
