## Amazon Connect Terraform Implementation: Flows, Queues, and Routing Profiles

Below is detailed, **separate content** for managing Amazon Connect **Contact Flows**, **Queues**, and **Routing Profiles** using Terraform Cloud, with configuration and JSON files as shown in your attached project structure[1].

---

## **Contact Flows**

**Purpose:**  
Contact flows define the logic for customer interactions in Amazon Connect (e.g., IVR menus, call routing, etc.).

**JSON Storage:**  
- Each flow is represented as a JSON file (e.g., `outbound_flow.json`, `sample_tf_flow.json`) in the `contact_flows` directory within your project structure[1].

**Terraform Usage:**  
- Use the `aws_connect_contact_flow` resource.
- Reference the JSON file using the `file()` function and assign its content to the `content` argument.

**Example:**

```hcl
resource "aws_connect_contact_flow" "example" {
  instance_id = var.instance_id
  name        = "Outbound Flow"
  type        = "CONTACT_FLOW"
  content     = file("${path.module}/contact_flows/outbound_flow.json")
  description = "Outbound contact flow"
  tags        = var.tags
}
```
- The `content` argument expects the JSON definition exported from Amazon Connect or via the AWS CLI[2][3].
- Each flow is managed as code, and changes to the JSON file will trigger Terraform updates.

---

## **Queues**

**Purpose:**  
Queues are "waiting areas" for contacts before they are routed to agents. They are critical for managing call distribution and agent workload.

**JSON Storage:**  
- Each queue is defined in a JSON file (e.g., `inbound_queue.json`, `outbound_queue.json`) under the `contact_queues` directory[1].

**Terraform Usage:**  
- Use the `aws_connect_queue` resource.
- Reference queue attributes (name, description, hours of operation, etc.) from the decoded JSON.

**Example:**

```hcl
locals {
  inbound_queue = jsondecode(file("${path.module}/contact_queues/inbound_queue.json"))
}

resource "aws_connect_queue" "inbound" {
  instance_id          = var.instance_id
  name                 = local.inbound_queue.name
  description          = local.inbound_queue.description
  hours_of_operation_id = local.inbound_queue.hours_of_operation_id
  max_contacts         = local.inbound_queue.max_contacts
  tags                 = var.tags
}
```
- Ensure all required fields (name, hours of operation, etc.) are present in the JSON[4][5].

---

## **Routing Profiles**

**Purpose:**  
Routing profiles link queues to agents and define which channels (voice, chat, etc.) and priorities apply. Each agent is assigned one routing profile, and each profile can include multiple queues[6][7][8].

**JSON Storage:**  
- Routing profiles are stored as JSON files (e.g., `routing_profile.json`, `routing_profiles.json`) in the `routing_profiles` directory[1].

**Terraform Usage:**  
- Use the `aws_connect_routing_profile` resource.
- Reference the JSON file, and use its properties for configuration.

**Example:**

```hcl
locals {
  routing_profile = jsondecode(file("${path.module}/routing_profiles/routing_profile.json"))
}

resource "aws_connect_routing_profile" "profile" {
  instance_id               = var.instance_id
  name                      = local.routing_profile.name
  description               = local.routing_profile.description
  default_outbound_queue_id = local.routing_profile.default_outbound_queue_id
  queue_configs {
    queue_id    = local.routing_profile.queue_configs[0].queue_id
    priority    = local.routing_profile.queue_configs[0].priority
    delay       = local.routing_profile.queue_configs[0].delay
    channel     = local.routing_profile.queue_configs[0].channel
  }
  media_concurrencies {
    channel     = local.routing_profile.media_concurrencies[0].channel
    concurrency = local.routing_profile.media_concurrencies[0].concurrency
  }
  tags = var.tags
}
```
- The `queue_configs` and `media_concurrencies` blocks are populated from the JSON, allowing you to manage queue priorities and channel concurrency per routing profile[6][7][8].

---

## **Best Practices & Workflow**

- **Modularization:** Reference reusable modules from a central repository for consistency.
- **Separation of Data and Logic:** Store all flows, queues, and routing profiles as JSON for easy editing and review.
- **Terraform Cloud Integration:** Connect your GitHub repo to a Terraform Cloud workspace; changes to JSON or Terraform files trigger automated plans and applies.
- **Environment Isolation:** Each environment (e.g., `projectA/us-east-1`, `projectB/us-west-2`) has its own folder and state, as shown in your structure[1].

---

## **Summary Table**

| Component      | Directory & Example File                | Terraform Resource                | Notes                                      |
|----------------|----------------------------------------|-----------------------------------|--------------------------------------------|
| Contact Flows  | `contact_flows/outbound_flow.json`     | `aws_connect_contact_flow`        | JSON content passed as `content`           |
| Queues         | `contact_queues/inbound_queue.json`    | `aws_connect_queue`               | JSON decoded, fields mapped to attributes  |
| Routing Profiles| `routing_profiles/routing_profile.json`| `aws_connect_routing_profile`     | JSON decoded, includes queue configs       |

---

This approach ensures that each Amazon Connect component is managed independently, version-controlled, and can be updated or rolled back as needed, all while leveraging the power of Terraform Cloud automation and GitHub collaboration.

Sources
[1] image.jpg https://pplx-res.cloudinary.com/image/upload/v1749712228/user_uploads/55846400/1b137519-3ccb-4000-8885-b926314e44c7/image.jpg
[2] aws-ia/terraform-aws-amazonconnect: Amazon Connect - GitHub https://github.com/aws-ia/terraform-aws-amazonconnect
[3] AWS Amazon Connect Contact Flow - Examples and best practices https://shisho.dev/dojo/providers/aws/Amazon_Connect/aws-connect-contact-flow/
[4] Amazon connect Queues using Terraform script - HashiCorp Discuss https://discuss.hashicorp.com/t/amazon-connect-queues-using-terraform-script/59928
[5] How to Manage Queues in Amazon Connect - CloudHesive https://www.cloudhesive.com/blog-posts/how-to-manage-queues-in-amazon-connect/
[6] How Amazon Connect uses routing profiles https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing.html
[7] Managing agent routing profiles with a new Amazon Connect API https://aws.amazon.com/blogs/contact-center/managing-agent-routing-profiles-with-a-new-amazon-connect-api/
[8] Create a routing profile in Amazon Connect to link queues to agents https://docs.aws.amazon.com/connect/latest/adminguide/routing-profiles.html
[9] aws_connect_contact_flow | Resources | hashicorp/aws | Terraform https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/connect_contact_flow
[10] aws_connect_contact_flow_mod... https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/connect_contact_flow_module
[11] Flows in Amazon Connect - AWS Documentation https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-flows.html
[12] Customer Service Software - Cloud Contact Center - Amazon Connect https://aws.amazon.com/connect/
[13] aws_connect_queue | Resources | hashicorp/aws - Terraform Registry https://registry.terraform.io/providers/hashicorp/aws/5.86.1/docs/resources/connect_queue
[14] aws-4-49-0_connect_queue | Resources - Terraform Registry https://registry.terraform.io/providers/figma/aws-4-49-0/latest/docs/resources/connect_queue
[15] aws_connect_routing_profile | Resources | hashicorp/aws | Terraform https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/connect_routing_profile
[16] aws_connect_routing_profile | Data Sources | hashicorp/aws https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/connect_routing_profile
[17] Amazon Connect Security Profiles can not be updated #2046 - GitHub https://github.com/hashicorp/terraform-provider-awscc/issues/2046
[18] AWS On Air WWPS Summit 2022 ft. Contact Center as Code https://www.youtube.com/watch?v=UUrwTTmytr8
[19] Automate Microsoft web application deployments with GitHub ... - AWS https://aws.amazon.com/blogs/modernizing-with-aws/automate-microsoft-web-application-deployments-with-github-actions-and-terraform/
[20] A Practitioner's Guide to Using HashiCorp Terraform Cloud with ... https://www.hashicorp.com/en/resources/a-practitioner-s-guide-to-using-hashicorp-terraform-cloud-with-github
[21] AWS connect contact flow error while creating a script https://repost.aws/questions/QUrVzPDkU2SYGuOXoZArS0PA/aws-connect-contact-flow-error-while-creating-a-script
[22] Using the Terraform AWS Cloud Control provider for managing AWS ... https://aws.amazon.com/blogs/hpc/using-the-terraform-aws-cloud-control-provider-for-managing-aws-batch-resources/
[23] Amazon Connect: Contact Center as Code — Part 1 - Ahmed Bebars https://blog.abebars.io/amazon-connect-contact-center-as-code-part-1-5b2297a2e0d3
[24] How to Use AWS Service Catalog with HashiCorp Terraform Cloud https://aws.amazon.com/blogs/apn/how-to-use-aws-service-catalog-with-hashicorp-terraform-cloud/
[25] Get started with Terraform Cloud using GitHub and AWS. https://gist.github.com/isaacarnault/ed11132744fb3a1d554985477ef6cdcd
[26] Aws_connect_queue issue? - Terraform Providers https://discuss.hashicorp.com/t/aws-connect-queue-issue/59518
[27] Get ID of Amazon Connect - Basic Routing Profile to use in ... https://stackoverflow.com/questions/75876185/get-id-of-amazon-connect-basic-routing-profile-to-use-in-aws-connect-user-te
[28] AWS Routing Profile access control tags Terraform/Github https://discuss.hashicorp.com/t/aws-routing-profile-access-control-tags-terraform-github/69502
