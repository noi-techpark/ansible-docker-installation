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

## Versioning

In order to have a verioning in place and working, create leightweight tags that point to the appropriate minor release versions.

Creating a new minor release:

```bash
git tag 1.0
git push --tags
```

Replacing an already existing minor release:

```bash
git tag -d 1.0
git push origin :refs/tags/1.0
git tag 1.0
git push --tags
```
