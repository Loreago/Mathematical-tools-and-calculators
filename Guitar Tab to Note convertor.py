note_list={0:["C"],1:["C#","Db"],2:["D"],3:["D#","Eb"],4:["E"],5:["F"],6:["F#","Gb"],7:["G"],8:["G#","Ab"],9:["A"],10:["A#","Bb"],11:["B"]}

def tab_formatting(string:str,fret:int):
    for items in note_list:
        if string in note_list[items]:
            value=int(items)
            break
    note=note_list[(value+fret)%12]
    return note

if __name__=="__main__":
    user_string=input("What note is your string? (case sensitive): ")
    user_fret=int(input("What fret is your note on? "))
    user_note=tab_formatting(user_string,user_fret)
    if len(user_note)>1:
        print(f"The note on the {user_fret} fret on the {user_string} string is {user_note[0]}/{user_note[1]}")
    else:
        print(f"The note on the {user_fret} fret on the {user_string} string is {user_note[0]}")