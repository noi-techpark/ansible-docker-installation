import json
import subprocess
import time

timeout = 60 * 5    # 5 minutes

healthy_statuses = set(['healthy', 'up'])
unhealthy_statuses = set(['down', 'unhealthy', 'removed'])
stabilized_statuses = healthy_statuses | unhealthy_statuses

def executeCommand(command, stdin=None):
    process = subprocess.Popen(command, shell=True, cwd=None, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = process.communicate(input=(stdin.encode() if stdin != None else None))[0]

    output = stdout.decode("utf-8")

    if process.returncode != 0:
        print('Command failed: ' + command)
        exit(-1)

    return output

def parseJson(text):
    return json.loads(text)

def getContainerStatus(container_id):
    command = 'docker inspect --format="{{{{json .State}}}}" {0}'.format(container_id)
    container_information = parseJson(executeCommand(command))
    
    return extractStatus(container_information)

def extractStatus(container_information):
    if 'Health' in container_information:
        return container_information['Health']['Status']
    else:
        return container_information['Status']

def isStatusStable(status):
    return status in stabilized_statuses

def isStatusHealthy(status):
    return status in healthy_statuses

def areContainersStable(container_ids):
    for container_id in container_ids:
        container_state = getContainerStatus(container_id)

        if not isStatusStable(container_state):
            return False

    return True

def areContainersHealthy(container_ids):
    for container_id in container_ids:
        container_state = getContainerStatus(container_id)

        if not isStatusHealthy(container_state):
            return False

    return True

def main():
    start_time = time.time()

    container_ids = executeCommand('docker-compose ps --quiet').splitlines()

    # Wait until containers are stable
    while True:
        if areContainersStable(container_ids):
            break

        # Sleep with timeout
        if time.time() > start_time + timeout:
            print('Timeout')
            exit(-1)

        time.sleep(1)

    # Check container health
    if not areContainersHealthy(container_ids):
        print('Containers are unhealthy')
        exit(-1)

if __name__ == "__main__":
    main()
