from PIL.ImageCms import Flags

import docker_helper
import tariere
from time import sleep

def main():
    docker_helper.stop_and_remove_all(['passoire_test','passoire_nh'])
    passoire = docker_helper.get_and_run_passoire(
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
        input("Press Enter to stop the container...")
        docker_helper.stop_and_remove_all(['passoire_test','passoire_nh'])

if __name__ == '__main__':
    main()