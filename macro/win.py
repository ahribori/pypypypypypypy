import pywinauto
from pywinauto import application

app = application.Application(backend="uia")

procs = pywinauto.findwindows.find_elements()

for proc in procs:
    # print(proc.process_id, proc.name)

    # 특정 윈도우를 찾는다.
    if "메모장" in proc.name:
        app = application.Application(backend="uia").connect(process=proc.process_id)

        # 컨트롤을 얻는다
        dialog = app.top_window()
        dialog.print_control_identifiers()

        # 특정 영역의 position을 구한다.
        rect = dialog.Edit.rectangle()
        x = rect.left
        y = rect.top
        width = rect.right - rect.left
        height = rect.bottom - rect.top

        print(rect)
        print(x, y, width, height)
        break
