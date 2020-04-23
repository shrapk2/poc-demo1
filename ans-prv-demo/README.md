# ans-prv-demo

## Description

Provisioning role for poc-demo Python code to AWS Lambda

```bash
.
├── playbook.yml
├── README.md
├── ansible.cfg
└── roles
    └── ans-prv-demo
        ├── defaults
        │   └── main.yml
        ├── meta
        │   └── main.yml
        └── tasks
            └── main.yml
```

## Requirements

Local Requirements

- A local system capable of running Ansible
- A local system with the latest
  - Python/2.7.15

## Role Variables

The following variables need to be defined to properly execute this role

- ans_repo_path
- aws_lambda_function_name
- aws_acc_key
- aws_svc_key
- aws_region
- aws_lambda_role

## Role Tags

An explanation of any tags used/required within the role

- `always`: Ansible default, skips all tasks assigned this tag
- `never`: Ansible default, skips all tasks assigned this tag
- `create`: Custom tag, Creates all artifacts for an AWS Lambda function
- `execute`: Custom tag, Execute AWS Lambda function

## Dependencies

None at this time

## Example Playbook

Below is an example of a _playbook.yml_ file that will execute each role.

```yaml
- hosts: all
  gather_facts: true
  name: Provisioning role for poc-demo Python code to AWS Lambda
  become: no

  vars:
    var1: value
    var2: value

  roles:
    - { role: ans-prv-demo, tags: ans-prv-demo }
```

## License

MIT

## Author Information

Kenney Sharpton II
