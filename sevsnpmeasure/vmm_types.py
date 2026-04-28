from enum import Enum, IntEnum, auto


class VMMType(Enum):
    QEMU = 1
    ec2 = 2
    gce = 3


class VMMVersion(IntEnum):
    VMM_LATEST = auto()
    VMM_V1 = auto()
    VMM_V2 = auto()


def get_vmm_version(vmm_type: VMMType, vmm_version: VMMVersion):
    latest_version = VMMVersion.VMM_V1
    if vmm_type == VMMType.ec2:
        latest_version = VMMVersion.VMM_V2
    if vmm_version == VMMVersion.VMM_LATEST:
        vmm_version = latest_version
    if vmm_version > latest_version:
        raise ValueError("Unsupported VMM version {} for {}".format(vmm_version.name, vmm_type.name))
    return vmm_version
