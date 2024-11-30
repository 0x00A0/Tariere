

import docker_helper
import tariere
import csv
from time import sleep

image_names = [
    'noorabh/group4_passoire:latest',
    'katjawi23/passoire_base:latest',
    'jadypamella/passoire:latest',
#    'nharrand/passoire:latest', 
    '0x00a0/passoire_group06:latest'
]


def main():
    docker_helper.stop_and_remove_all(['passoire_test','passoire_nh'])
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
        sleep(10)
        try:
            flags = {}
            # flags.update(tariere.ssh_backdoor())
            # tariere.http_get()
            tariere.sql()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            #docker_helper.stop_and_remove_all(['passoire_test','passoire_nh'])
            print(f"\033[1;42mFlags found: {len(flags)}\033[0m")
            # save to csv, named after the image
            with open(f'flags/{image_name.replace("/","_").replace(":","_")}.csv', mode='w') as file:
                writer = csv.writer(file, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                writer.writerows(flags.items())
            

if __name__ == '__main__':
    main()