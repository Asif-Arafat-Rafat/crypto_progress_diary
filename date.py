from datetime import date
import os
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
def file_name(coins):
    today = date.today()
    print("Today's date:", today)
    filename = f"TradingData_{today}.xlsx"
    # filename = "trial.xlsx"
    current_dir=os.path.dirname(os.path.abspath(__file__))
    path=os.path.join(current_dir,"sub")
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(os.path.join(path,filename)):
        wb=Workbook()
        ws=wb.active
        ws.append(["Coin Name"])
        ws.title="date=="+str(today)
        wb.save(os.path.join(path,filename))
    wb=load_workbook(os.path.join(path,filename))
    ws=wb.active
    found=False
    mxc=ws.max_column
    ws[get_column_letter(mxc+1)+str(1)]=str(today)
    for key,value in coins.items():
        for i in range(1,ws.max_row):
            if(key==ws["A"+str(i)].value):
                ws[get_column_letter(mxc)+str(i)]=value
                found=True
                break
        if not found:
            ws["A"+str(ws.max_row+1)]=key
            ws[get_column_letter( mxc+1)+str( ws.max_row)]=value
        else:
            found=False

    wb.save(os.path.join(path,filename))