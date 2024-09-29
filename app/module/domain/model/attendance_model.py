from dataclasses import dataclass

@dataclass
class Attendance:
    attendance_path: str

    def __post_init__(self):
        if not self._validate_key_start_20year(self.attendance_path):
            raise ValueError(f"attendance_path must start with '20': {self.attendance_path}")

    def _validate_key_start_20year(self, key: str) -> bool:
        return key.startswith("20")
