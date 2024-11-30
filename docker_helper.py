import docker

def get_and_run_passoire(image_name = 'nharrand/passoire:latest', env: dict = None, ports: dict = None):
    client = docker.from_env()
    print(f"\033[1;46mPulling image {image_name}...\033[0m")
    client.images.pull(image_name)
    print(f"\033[1;46mImage {image_name} is pulled.\033[0m")
    container = client.containers.run(
        image_name,
        detach=True,
        environment=env,
        ports=ports
    )
    print(f"\033[1;46mContainer {container.name} (ID: {container.short_id}) is running.\033[0m")
    return container

def stop_and_remove_all(containers_to_keep):
    client = docker.from_env()

    if isinstance(containers_to_keep, str):
        containers_to_keep = [containers_to_keep]

    containers = client.containers.list(all=True)

    for container in containers:
        if container.name in containers_to_keep:
            # print(f"\033[1;46mSkipping container {container.name}, as it is to be kept.")
            continue
        try:
            if container.status in ["running", "restarting", "paused"]:
                print(f"\033[1;46mStopping container {container.short_id}...\033[0m")
                container.stop()

            print(f"\033[1;46mRemoving container {container.short_id}...\033[0m")
            container.remove()
            print(f"\033[1;46mContainer {container.short_id} has been removed.\033[0m")
        except Exception as e:
            print(f"\033[1;46mAn error occurred with container {container.short_id}: {e}\033[0m")
