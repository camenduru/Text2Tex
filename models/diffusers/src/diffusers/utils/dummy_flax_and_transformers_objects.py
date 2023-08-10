# This file is autogenerated by the command `make fix-copies`, do not edit.
# flake8: noqa

from ..utils import DummyObject, requires_backends


class FlaxStableDiffusionImg2ImgPipeline(metaclass=DummyObject):
    _backends = ["flax", "transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["flax", "transformers"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["flax", "transformers"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["flax", "transformers"])


class FlaxStableDiffusionInpaintPipeline(metaclass=DummyObject):
    _backends = ["flax", "transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["flax", "transformers"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["flax", "transformers"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["flax", "transformers"])


class FlaxStableDiffusionPipeline(metaclass=DummyObject):
    _backends = ["flax", "transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["flax", "transformers"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["flax", "transformers"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["flax", "transformers"])