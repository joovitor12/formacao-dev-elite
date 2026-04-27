class AppError(Exception):
    """Erro de domínio da aplicação (mapeado para HTTP em handlers)."""

    def __init__(self, message: str, status_code: int = 400) -> None:
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class NotFoundError(AppError):
    def __init__(self, message: str = "Recurso não encontrado") -> None:
        super().__init__(message, status_code=404)
