# -*- coding: utf-8 -*-

def main():
    softreset('192.168.1.21')


def softreset(_host):
    from subprocess import call
    call(["net", "rpc", "shutdown", "-r", "-I", _host, "-U", "Administrador%SemParar"])

if __name__ == "__main__":
    main()

