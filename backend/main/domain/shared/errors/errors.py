class DomainException(Exception):
    def __init__(self, *args: object) -> None:
        self._message = args[0]
        super().__init__(*args)

    def message(self) -> str:
        return self._message  # type: ignore


class ProhibitedGenerationError(DomainException):
    """禁止された生成を表すエラー"""

    pass
