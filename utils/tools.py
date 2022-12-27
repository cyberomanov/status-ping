from datatypes.server import Server


def get_server_instances(servers: dict[str, str]) -> list[Server]:
    instances = []
    for server in servers.items():
        instances.append(Server(name=server[0], host=server[1]))
    return instances
