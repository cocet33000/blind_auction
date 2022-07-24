class DomainException(Exception):
    pass


class ProhibitedGenerationError(DomainException):
    """禁止された生成を表すエラー"""

    pass
