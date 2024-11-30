from tkinter import image_names

from PIL.ImageCms import Flags

import docker_helper
import tariere
from time import sleep

def main():
    docker_helper.stop_and_remove_all(['passoire_test','passoire_nh'])
    image_names=['nharrand/passoire:latest', '0x00a0/passoire_group06:latest']
    for image_name in image_names:
        print("\033[1;41m",'#'*50,"\033[0m")
        print(f"\033[1;41m Attacking image {image_name}\033[0m ")
        print("\033[1;41m",'#'*50,"\033[0m")
        passoire = docker_helper.get_and_run_passoire(
            image_name=image_name,
            env={
                "GROUP_SECRET": "3833fa622ce58c76782d5505e72d4a13b0b91c01",
                "HOST": "localhost"
            },
            ports={
                "80/tcp": 10080,
                "3002/tcp": 13002,
                "22/tcp": 10022,
                "3306/tcp": 13306
            }
        )
        sleep(5)
        try:
            flags = {}
            flags.update(tariere.ssh_backdoor())
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            docker_helper.stop_and_remove_all(['passoire_test','passoire_nh'])
            print(f"\033[1;42mFlags found: {len(flags)}\033[0m")

if __name__ == '__main__':
    main()