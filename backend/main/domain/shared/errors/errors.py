class DomainException(Exception):
    def __init__(self, *args: object) -> None:
        try:
            self._message = args[0]
        except:
            self._message = "no message"

        super().__init__(*args)

    def message(self) -> str:
        return self._message  # type: ignore


class ProhibitedGenerationError(DomainException):
    """禁止された生成を表すエラー"""

    pass
