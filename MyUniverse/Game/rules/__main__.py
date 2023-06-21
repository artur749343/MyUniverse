import json, os

def rules(**kwargs):
    other=json.load(open("\\".join(str(os.path.abspath(__file__)).split("\\")[:-3])+"\\Game\\game\\other.json", 'r', encoding="utf-8"))
    other["rules"]=[[key, f] for key, f in kwargs.items()]
    json.dump(other, open("\\".join(str(os.path.abspath(__file__)).split("\\")[:-3])+"\\Game\\game\\other.json", 'w', encoding="utf-8"))


main_callable=rules