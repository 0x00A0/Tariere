import docker

def get_and_run_passoire(image_name = 'nharrand/passoire:latest', env: dict = None, ports: dict = None):
    client = docker.from_env()
    print(f"Pulling image {image_name}...")
    client.images.pull(image_name)
    print(f"Image {image_name} is pulled.")
    container = client.containers.run(
        image_name,
        detach=True,
        environment=env,
        ports=ports
    )
    print(f"Container {container.name} (ID: {container.short_id}) is running.")
    return container

def stop_and_remove_all(containers_to_keep):
    client = docker.from_env()

    if isinstance(containers_to_keep, str):
        containers_to_keep = [containers_to_keep]

    containers = client.containers.list(all=True)

    for container in containers:
        if container.name in containers_to_keep:
            print(f"Skipping container {container.name}, as it is to be kept.")
            continue
        try:
            if container.status in ["running", "restarting", "paused"]:
                print(f"Stopping container {container.name}...")
                container.stop()

            print(f"Removing container {container.name}...")
            container.remove()
            print(f"Container {container.name} has been removed.")
        except Exception as e:
            print(f"An error occurred with container {container.name}: {e}")


# test
if __name__ == '__main__':
    passoire = get_and_run_passoire(
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
    input("Press Enter to stop the container...")
    stop_and_remove_all(['passoire_test','passoire_nh'])