class DomainException(Exception):
    def __init__(self, *args: object) -> None:
        try:
            self._message = args[0]
        except Exception as e:
            self._message = "no message" + str(e)

        super().__init__(*args)

    def message(self) -> str:
        return self._message  # type: ignore


class ProhibitedGenerationError(DomainException):
    """禁止された生成を表すエラー"""

    pass
