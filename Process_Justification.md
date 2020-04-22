# Process_Justification

Problem Statement: Why run this a serverless or container? Defend position.

---

## Response

For purposes of this sample project, I decided to execute the requirement within an AWS Lambda function versus container. While I'm proficient at both, running this simple function serverless proved to consume much less resources and costs compared to deploying a container with AWS Fargate or other container-based service.

> I could have run as a local container, however, I decided to execute as I would a production resource versus a simple test case

Beyond this proof of concept, as a rule, I always recommend serverless/containerization over virtual machines due to today's public cloud "world". A majority of organizations are moving or have moved into the public cloud space (AWS/GCP/Azure); the dichotomy of this migration to an "instant computing" environment is the costs of doing so. These providers charge for resources based on capacity and time. Containers/serverless provide the most optimized services for both. While both these costs are also true with on premise IT infrastructure, the cost of ownership is perpetual in the public cloud and unlimited in theory, versus "finite" of purchasing physical servers for a datacenter.

I do not completely eliminate the justification for a traditional virtual machine, as there are always edge cases that require the isolated computing power or features that are otherwise difficult to obtain via serverless/container system.

Few examples include:

- Imagine building (ISO, Kickstart, OVA, etc.)
- Kubernetes/Container hosts

As for physical/bare metal, I rarely recommend dedicated hardware for anything short of hypervisors or container hosts. Running bare metal simply isn't cost effective in today's computing environment; short for extremely rare ultra-high performance requirements or security (i.e. air-gapped) systems.

## Caveats

Above are my basic ethos into which platforms I'd chose, there are always external requirements that can drive the direction of the solution.

For every solution, they must always within at least:

- Business requirements
- Security requirements
