import typing as tp

from kubernetes import client
from pydantic import field_serializer, Field

from .base import BaseKubernetesManifestObject
from .v1_resource_claim import V1ResourceClaim


class ResourcesObject(BaseKubernetesManifestObject):
    cpu: str
    memory: str
    nvidia_gpu: str = Field(..., alias='nvidia.com/gpu')


class V1ResourceRequirements(BaseKubernetesManifestObject[client.V1ResourceRequirements]):
    _kube_type = client.V1ResourceRequirements

    claims: tp.Optional[tp.List[V1ResourceClaim]] = None
    requests: tp.Optional[ResourcesObject] = None
    limits: tp.Optional[ResourcesObject] = None
