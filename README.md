# MySimpleNeutronPlugin
Sample Neutron Plugin  

## This Tutorial aims to build the sample neutron plugin in step by step mode. 

## Prerequisties :

	1. Running Devstack

	Note :  I use liberty version

## Exercise1:

### Objective : Write the very basic neutron plugin (dummy - without any error)

### Steps for setting up :

 a.  Neutron plugins are located in  "neutron/plugins" directory. Each plugin is a folder.
 	 In devstack it is "/opt/stack/neutron/neutron/plugins". By default the few plugins are installed 
 	  bigswitch  brocade  common  embrane  hyperv  ml2  myplugin  nuage  oneconvergence  opencontrail
 b.  create a directory name for your plugin 
 	 In my exaample "MySimpleNeutronPlugin"
 c.  copy the plugin.py and __init__.py to this folder
 d.	 Modify the /etc/neutron/neutron.conf as below,
 		comment the service_plugins and ml2 core plugin as below
 			#service_plugins = neutron.services.l3_router.l3_router_plugin.L3RouterPlugin
 			#core_plugin = neutron.plugins.ml2.plugin.Ml2Plugin
 		add the new core_plugin points to your plugin file
 			core_plugin = neutron.plugins.MySimpleNeutronPlugin.plugin.MyPlugin

 		The plugin syntax is as below,
 			core_plugin = neutron.plugins.<your plugin directory>.<plugin file name>.<plugin class name>

 e.  Restart the neutron service 
 		In devstack, goes to the q-svc screen, press CTRL+C. and uparrow(neutron start command) and enter it.


 ### Code explained :
 	1. we need do have dummy __init__.py file to load the plugin. Otherwise neutron couldnt load this plugin.
 	2. Plugin should be derived from the neutron plugin base class neutron_plugin_base_v2.NeutronPluginBaseV2
 	3. Plugin should have the following basic functions defined
 		create_network, create_port, create_subnet, delete_network, delete_port, delete_subnet, get_network, get_networks, get_port, get_ports, get_subnet, get_subnets, update_network, update_port, update_subnet
 	4. Thats all



## References

1)

http://www.slideshare.net/salv_orlando/how-to-write-a-neutron-plugin-if-you-really-need-to
https://github.com/salv-orlando/hdn

2)
http://control-that-vm.blogspot.fr/2014/02/neutron-plugin-architecture.html
http://control-that-vm.blogspot.fr/2014/02/writing-your-own-neutron-plugin.html
http://control-that-vm.blogspot.fr/2014/02/modifiying-neutron-plugin-and.html
http://fosshelp.blogspot.fr/search/label/OpenStack%20Neutron