Ansible Docker Installation Role
================================

Installation of a Docker server.

Role Variables
--------------

- `docker_compose_version`: The version of docker-compose that should be installed

Example Playbook
----------------

    - hosts: servers
      roles:
        - role: ansible-docker-installation
          docker_compose_version: 1.25.4
