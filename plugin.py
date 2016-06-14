from neutron import neutron_plugin_base_v2

class MyPlugin(neutron_plugin_base_v2.NeutronPluginBaseV2):

    def __init__(self):
        pass


    def create_network(self,context,network):
        return network

    def update_network(self,context,id,network):
        return network

    def get_network(self,context,id,fields=None):
        network = { }
        return network

    def get_networks(self,context,filters=None,fields=None):
        network = { }
        return network

    def delete_network(self,context,id):
        return id


    def create_port(self,context,port):
        return port

    def update_port(self,context,id,port):
        return port
    def get_port(self,context,id,fields=None):
        port = {}
        return port
    def get_ports(self,context,filters=None,fields=None):
        port = {}
        return port
    def delete_port(self,context,id):
        return id


    def create_subnet(self,context,subnet):
        return subnet
    def update_subnet(self,context,id,subnet):
        return subnet
    def get_subnet(self,context,id,fields=None):
        subnet={}
        return subnet
    def get_subnets(self,context,filters=None,fields=None):
        subnet={}
        return subnet
    def delete_subnet(self,context,id):
        return id
