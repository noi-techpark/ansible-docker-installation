Ansible Docker Installation Role
================================

Installation of a Docker server.

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: ansible-docker-installation
```

## AWS IAM Role

In order for an AWS EC2 instance to be able to access AWS ECR, an IAM role must be attached to the EC2 instance to grant access.

1. **Create the AWS IAM role:**  
    - AWS service: EC2
    - Permissions:
      ```json
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Action": [
              "ecr:GetAuthorizationToken",
              "ecr:BatchCheckLayerAvailability",
              "ecr:GetDownloadUrlForLayer",
              "ecr:BatchGetImage"
            ],
            "Resource": "*"
          }
        ]
      }
      ```
2. **Attach the role to the EC2 instance**

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
