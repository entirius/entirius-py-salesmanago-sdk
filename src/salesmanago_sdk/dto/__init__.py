from dataclasses import asdict, dataclass


@dataclass
class DTO:
    def asdict(self) -> dict:
        return asdict(self)

    def to_dict(self):
        return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})
