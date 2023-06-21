import json, os

def formule(first:str="power",const:int=1,middle:str="speed",last:str="time"):
    other=json.load(open("\\".join(str(os.path.abspath(__file__)).split("\\")[:-3])+"\\Game\\game\\other.json", 'r', encoding="utf-8"))
    other["events"].append([first, const, middle, last])
    json.dump(other, open("\\".join(str(os.path.abspath(__file__)).split("\\")[:-3])+"\\Game\\game\\other.json", 'w', encoding="utf-8"))

main_callable=formule