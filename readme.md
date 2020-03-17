Ansible Docker Installation Role
================================

Installation of a Docker server.

## Role Variables

- `docker_installation_compose_version`: The version of docker-compose that should be installed

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: ansible-docker-installation
      vars:
        docker_installation_compose_version: 1.25.4
```
