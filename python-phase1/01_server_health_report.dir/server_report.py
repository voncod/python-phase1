import json

with open("servers.json", "r") as file:
    servers = json.load(file)

count_total_servers = 0
count_online_servers = 0
count_offline_servers = 0
environment_count = {}
online_servers_list = []
attention_required_list = []

for server in servers:
    count_total_servers += 1
    if server["status"] == "online":
        count_online_servers += 1
        
        online_servers = {
                "name": server["name"],
                "environment": server["environment"]
        }

        online_servers_list.append(online_servers)

    elif server["status"] == "offline":
        count_offline_servers += 1
        
        attention_servers_list = {
                "name": server["name"],
                "reason": server["status"]
        }
        
        attention_required_list.append(attention_servers_list)

    environment = server["environment"]

    if environment not in environment_count:
        environment_count[environment] = 0
           
    environment_count[environment] += 1
    
report = {
        "total_servers": count_total_servers,
        "online_servers": count_online_servers,
        "offline_servers": count_offline_servers,
        "by_environment": environment_count,
        "online_servers_list": online_servers_list,
        "attention_required_list": attention_required_list

}

with open("report.json", "w") as file:
    json.dump(report, file, indent=4)

