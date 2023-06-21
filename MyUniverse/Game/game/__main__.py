import os, json

def game(fps:int=60, size:int=10,*args:dict):
    all={"fps": fps, "size": size, "objects": args}
    json.dump(all, open(str(os.path.abspath(__file__))[:-11]+"game.json", 'w', encoding="utf-8"))
    os.system(str(os.path.abspath(__file__))[:-11]+"start.bat")

main_callable=game