from __future__ import annotations
from pathlib import Path
from typing import Union

class FilePath:
    def __init__(self, value: Union[str, Path]) -> None:
        self._value: Path = Path(value)

    def exists(self) -> bool:
        return self._value.exists()

    def raise_if_not_exists(self) -> None:
        assert self.exists(), FileNotFoundError(self._value)

    def as_string(self) -> str:
        return str(self._value)

    def parent_directory(self) -> DirectoryPath:
        return DirectoryPath(self._value.parent)

    def stem(self) -> FileName:
        return FileName(self._value.stem)

    def suffix(self) -> FileSuffix:
        return FileSuffix(self._value.suffix)


class DirectoryPath:
    def __init__(self, value: Union[str, Path]) -> None:
        self._value: Path = Path(value)

    def create(self) -> None:
        self._value.mkdir(parents=True, exist_ok=True)

    def join(self, file_name: FileName) -> FilePath:
        return FilePath(self._value / file_name.as_string())


class FileName:
    def __init__(self, value: str) -> None:
        self._value: str = str(value)

    def as_string(self) -> str:
        return self._value

    def sanitized(self) -> FileName:
        safe: str = self._value.replace("::", "__").replace("/", "-")
        forbidden: str = "<>:\\|?*\"\n\r\t"
        cleaned: str = "".join(ch for ch in safe if ch not in forbidden)[:200]
        return FileName(cleaned)


class SheetName:
    def __init__(self, value: str) -> None:
        self._value: str = str(value)

    def as_string(self) -> str:
        forbidden: str = ":\\/?*[]\""
        clean: str = "".join(ch for ch in self._value if ch not in forbidden)
        clean = self._handle_reserved(clean)
        return clean[:31] or "sheet"

    def _handle_reserved(self, name: str) -> str:
        return f"_{name}" if name.strip().lower() in {"history"} else name



class FileSuffix:
    def __init__(self, value: str) -> None:
        # Remove o ponto inicial se houver
        self._value: str = value.lstrip(".")

    def as_string(self) -> str:
        """Retorna o sufixo sem o ponto"""
        return self._value

    def with_dot(self) -> str:
        """Retorna o sufixo com o ponto"""
        return f".{self._value}" if self._value else ""

    def is_valid_for_tableau(self) -> bool:
        """Verifica se é um sufixo válido para arquivos Tableau"""
        tableau_formats: set[str] = {"twb", "twbx", "tds", "tdsx", "tde", "hyper"}
        return self._value.lower() in tableau_formats

    def is_archive(self) -> bool:
        """Verifica se é um formato de arquivo compactado"""
        archive_formats: set[str] = {"zip", "twbx", "tdsx", "tar", "gz", "7z"}
        return self._value.lower() in archive_formats

    def match(self, other: str) -> bool:
        """Compara com outro sufixo (case insensitive)"""
        return self._value.lower() == other.lstrip(".").lower()

    def __eq__(self, other: object) -> bool:
        if isinstance(other, FileSuffix):
            return self._value.lower() == other._value.lower()
        if isinstance(other, str):
            return self.matches(other)
        return False

    def __str__(self) -> str:
        return self.with_dot()

    def __repr__(self) -> str:
        return f"FileSuffix('{self._value}')"