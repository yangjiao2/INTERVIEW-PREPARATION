

- Which fields are required when writing a Kubernetes YAML manifest file for creating any type of Kubernetes resource?

apiVersion, kind, metadata


- What property of a Kubernetes service defines the set of pods that are accessed via the service?

The service's selector

- You need to utilize a PersistentVolume for application storage in a Kubernetes cluster. What field of a PersistentVolume can you use to control the number of nodes that can mount the PersistentVolume for reading and writing?

"accessMode" field: controls how many nodes can mount it for reading and writing. The supported values are ReadWriteOnce, ReadOnlyMany, and ReadWriteMany.

- after cordoned a node, what is the status of node?

SchedulingDisabled

- You have written a manifest file for a service in Kubernetes. You did not include the type field in the service's specification. What is the type of the service that will be created?

ClusterIP

- You have deployed an application in Kubernetes. The application container exposes port 80. You need to be able to access the application from outside of the cluster. What Kubernetes resource should you use to meet this requirement?

service

- In Kubernetes, what Pod field should you use to ensure that the code runs before the main application container starts?

initContainers

-  prefer to use Deployments rather than "naked" Pods (Pods that are not managed by a higher-level resource, such as a Deployment) for managing applications in Kubernetes? 

Deployments can reschedule pods that fai
Deployments support rolling updates and rollbacks
Deployments are compatible with Horizontal Pod Autoscalers

- volume vs. persistent volume?

A Volume's lifetime is the same as the lifetime of the pod that encloses it. PersistentVolumes have a lifetime independent of any pod allowing the data on a PersistentVolume to be reused by other pods.

Both Volumes and PersistentVolumes can be accessed by all of the containers in the pod enclosing them.

- If an application pod terminates, you would like to have the persistent volume remain but be able to delete its data. 

Ensure the volume is dynamically provisioned and change the reclaim policy of the PersistentVolume to "Retain"

- What is the recommended Kubernetes resource for running applications?

Deployment: easily scale and perform a rolling update to a new version using deployments. Deployments automatically maintain a ReplicaSet for replicating pods and are easier to work with than a ReplicaSet. 





