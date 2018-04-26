from telnetlib import Telnet
import sys

WAIT_TIME = 1


class CiscoAuto:

    def __init__(self, host, login_password, enable_password, port = 23):
        self.host = host
        self.login_password = login_password
        self.enable_password = enable_password
        self.port = port

    def login(self):
        self.tn = Telnet(self.host)
        ret = self.tn.read_until(b"Password: ", WAIT_TIME)
        print(ret.decode('utf-8'))
        self.tn.write(self.login_password.encode() + b"\n")
        ret = self.tn.read_until(b">", WAIT_TIME)
        print(ret.decode('utf-8'))


    def enable(self):
        self.tn.write(b"enable\n")
        ret = self.tn.read_until(b"Password: ", WAIT_TIME)
        self.tn.write(self.enable_password.encode() + b"\n")
        ret = self.tn.read_until(b"#", WAIT_TIME)
        print(ret.decode('utf-8'))


    def enter_configure_mode(self):
        self.tn.write(b"conf t\n")
        ret = self.tn.read_until(b"(config)#", WAIT_TIME)
        print(ret.decode('utf-8'))


    def shutdown(self):
        self.tn.write(b"interface FastEthernet 0\n")
        ret = self.tn.read_until(b"(config-if)#", WAIT_TIME)
        print(ret.decode('utf-8'))
        self.tn.write(b"shutdown\n")
        ret = self.tn.read_until(b"(config-if)#", WAIT_TIME)
        print(ret.decode('utf-8'))
        self.tn.write(b"exit\n")
        ret = self.tn.read_until(b"(config)#", WAIT_TIME)
        print(ret.decode('utf-8'))


    def exit_from_config(self):
        self.tn.write(b"exit\n")
        ret = self.tn.read_until(b"#", WAIT_TIME)
        print(ret.decode('utf-8'))

    def exit_from_enable(self):
        self.tn.write(b"exit\n")
        ret = self.tn.read_until(b"#", WAIT_TIME)
        print(ret.decode('utf-8'))

    def quit(self):
        self.tn.write(b"exit\n")
        self.tn.close()


if __name__ == '__main__':
    args = sys.argv

    router_script = CiscoAuto(args[1], args[2], args[3])
    router_script.login()
    router_script.enable()
    router_script.enter_configure_mode()
    router_script.shutdown()
    router_script.exit_from_config()
    router_script.exit_from_enable()
    router_script.quit()


