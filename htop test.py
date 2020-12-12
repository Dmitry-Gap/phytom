import psutil



TEMPLATES = {
    "cpu": {
        "loads": "Running Process: \n\t{}",
    }
}


CORE_LOAD_TEMPLATE = "core {0} --> |{1}|%\n\t"


TEMPLATES_LOAD_CORE = {
    "core":{
        "load" : "CPU load : \n\t{}"
    }
}



TEMPLATES_CPU_TIMES = {
    "cpu":{
        "times": "Times CPU : \n\tuser --> |{user}|\n\tsystem --> |{system}|\n\tidle --> |{idle}|"      
    }
}

TEMPLATES = {
    "mem": {
           "memory": "Disks space  : \n\ttotal --> |{total}|\n\tfree --> |{free}|\n\tpercent --> |{percent}|"
    }
} 

def get_meme():
    times = psutil.cpu_times(percpu = False)
    svmem = psutil.virtual_memory()
    load = psutil.cpu_percent(interval = 1, percpu = True) 
    res = {
        "load": {"values": load},
        "memory": {"total": svmem.total, "free": svmem.free, "percent":svmem.percent},
        "times": {"user": times.user, "system": times.system, "idle": times.idle
        }
    }
    return res

def show():
    cpu  = get_meme()
    template_load = ""
    for i, value in enumerate(cpu["load"]["values"]):
        template_load += CORE_LOAD_TEMPLATE.format(i, value)
    cpu_load_info = TEMPLATES_LOAD_CORE["core"]["load"].format(
        template_load
    )
    print(cpu_load_info)
    cpu_times_info = "" 
    cpu_times_info = TEMPLATES_CPU_TIMES["cpu"]["times"].format(**cpu["times"])
    print(cpu_times_info) 
    cpu_work_info = TEMPLATES["mem"]["memory"].format(**cpu["memory"])
    print(cpu_work_info)


if __name__ == "__main__":
    show()




PROCESS_ITER_TEMPLATE = " |Process|{} --> |{}|\n\t"

PROCESS_TEMPLATES = {
    "process": {
        "start": "Running Process: \n\t{}",
    }
}

def get_proc():
    proses = psutil.process_iter()
    var = {
        "proces": {"valu": proses}
    }
    return var

def informac():
    pros = get_proc()
    template_proc = ""
    for a, inf in enumerate(pros["proces"]["valu"]):
        template_proc += PROCESS_ITER_TEMPLATE.format(a, inf)
    cpu_proc_info = PROCESS_TEMPLATES["process"]["start"].format(
        template_proc
    )
    print(cpu_proc_info)
   
  
if __name__ == "__main__":
    informac()

TEMPLATES_NETWORK= {
    "net": {
           "nerwork": "Network info : \n\tbytes_sent --> |{bytes_sent}|\n\tbytes_recv --> |{bytes_recv}|\n\tpackets_sent--> |{packets_sent}|\n\tpackets_recv --> |{packets_recv}|\n\t"
    }
} 

def get_net():
       snetio = psutil.net_io_counters( pernic = False , nowrap = True )
       giv = {
        "nerwork": {"bytes_sent": snetio.bytes_sent, "bytes_recv": snetio.bytes_recv, "packets_sent":snetio.packets_sent, "packets_recv":snetio.packets_recv},
    }
       return giv

def show_network_info():
    info_net  = get_net()
    network_info = TEMPLATES_NETWORK["net"]["nerwork"].format(**info_net["nerwork"])
    print(network_info)


if __name__ == "__main__":
    show_network_info()

TEMPLATES_BATTERY= {
    "bat": {
           "battery": "Battery info : \n\tpercent --> |{percent}%|\n\tpower_plugged --> |{power_plugged}|\n\t"
    }
} 

def get_batt():
       sbattery = psutil.sensors_battery() 
       gev = {
        "battery": {"percent": sbattery.percent, "power_plugged": sbattery.power_plugged}
    }
       return gev

def show_battery_info():
    info_bat  = get_batt()
    network_battery = TEMPLATES_BATTERY["bat"]["battery"].format(**info_bat["battery"])
    print(network_battery)


if __name__ == "__main__":
    show_battery_info()    