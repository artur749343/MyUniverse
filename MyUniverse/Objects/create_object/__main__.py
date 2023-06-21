def object(pos:{'widget_name':'literal_entry','type':list}=[0, 0], power:int=100, all:dict={}, **kwargs):
    t={"space":pos,"power":power}
    t.update(all)
    for ia, xa in all.items():
        if ia in kwargs: t[ia]=[kwargs[ia]]+all[ia]
    return t

main_callable=object