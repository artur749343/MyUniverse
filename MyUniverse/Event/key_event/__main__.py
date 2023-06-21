import pygame, json, os
pygame.init()
def key_event(**kwargs:str):
    other=json.load(open("\\".join(str(os.path.abspath(__file__)).split("\\")[:-3])+"\\Game\\game\\datas.json", 'r', encoding="utf-8"))
    other["events"]=[[pygame.key.key_code(key), f] for key, f in kwargs.items()]
    json.dump(other, open("\\".join(str(os.path.abspath(__file__)).split("\\")[:-3])+"\\Game\\game\\datas.json", 'w', encoding="utf-8"))

main_callable=key_event