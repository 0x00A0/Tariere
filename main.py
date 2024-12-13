

import docker_helper
import tariere
import csv
from time import sleep

image_names = []



def main():
    # read target lists from file targets.txt
    with open('targets.txt', 'r') as file:
        for line in file:
            image_names.append(line.strip())
    
    docker_helper.stop_and_remove_all(['passoire_test','passoire_nh'])
    for image_name in image_names:
        print("\033[1;41m",'#'*50,"\033[0m")
        print(f"\033[1;41m Attacking image {image_name}\033[0m ")
        print("\033[1;41m",'#'*50,"\033[0m")
        passoire = docker_helper.get_and_run_passoire(
            image_name=image_name,
            env={
                #"GROUP_SECRET": "3833fa622ce58c76782d5505e72d4a13b0b91c01",
                "HOST": "localhost"
            },
            ports={
                "80/tcp": 2080,
                "3002/tcp": 2002,
                "22/tcp": 2022,
                "3306/tcp": 2306
            }
        )
        sleep(15)
        try:
            flags = {}
            sleep(10)
            flags.update(tariere.ssh_backdoor())
            sleep(10)
            flags.update(tariere.http_get())
            #tariere.sql()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            docker_helper.stop_and_remove_all(['passoire_test','passoire_nh'])
            print(f"\033[1;42mFlags found: {len(flags)}\033[0m")
            # save to csv, named after the image
            with open(f'flags/{image_name.replace("/","_").replace(":","_")}.csv', mode='w',newline='') as file:
                writer = csv.writer(file, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                writer.writerows(flags.items())
            

if __name__ == '__main__':
    main()