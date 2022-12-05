import lib_mcbox_tools
import lib_mcbox_network
def makeOnlineCommand(serverIP="127.0.0.1"):
    return "start n2n.exe -l " + serverIP + " -c playaaa"
lib_mcbox_network.checkNetwork()
command = makeOnlineCommand()
print("I am going to run:" + command)
r = lib_mcbox_tools.mcboxExec(command)
print(r)
