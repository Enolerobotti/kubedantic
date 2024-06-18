import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1PhotonPersistentDiskVolumeSource(BaseKubernetesManifestObject[client.V1PhotonPersistentDiskVolumeSource]):
    _kube_type = client.V1PhotonPersistentDiskVolumeSource

    fs_type: tp.Optional[str] = Field(None, alias='fsType')
    pd_id: tp.Optional[str] = Field(None, alias='pdID')
