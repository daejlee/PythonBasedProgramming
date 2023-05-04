import calendar as cal
import tkinter as tk

#tkinter 초기화
root = tk.Tk()
widget1 = tk.Text(root, width=20, height=10)

#calendar 모듈에서 2023년 5월 달력을 가져와 화면에 삽입
widget1.insert(1.0, cal.month(2023, 5))

widget1.pack()
root.mainloop()