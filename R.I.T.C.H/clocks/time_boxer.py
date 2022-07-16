

def make_time_boxes():
    time_boxes = []
    time_boxes_dict = {}
    start_time = "07:00"
    end_time = "23:00"

    for i in range(16):
        hour = start_time[0:2]
        for i in range(4):
            minute = start_time[3:]
            new_time = f"{hour}:{int(minute)+15}"
            if int(new_time[3:])>59:
                inted_time = int(new_time[0:2])+1
                if len(str(inted_time))<2:
                    inted_time="0"+str(inted_time)
                new_time = f"{inted_time}:00"
            time_boxes.append(f"{start_time}-{new_time}")
            start_time = new_time

    quarter=1
    for i in time_boxes:
        time_boxes_dict[i] = {}
        
        time_boxes_dict[i]["Time Quarter"] = f"{quarter}/64"
        time_boxes_dict[i]["Task_Scheduled"] = []
        quarter+=1
    return time_boxes_dict


