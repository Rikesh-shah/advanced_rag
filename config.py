from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

STORAGE_DIR = BASE_DIR / "storage"
REPOSITORIES_DIR = STORAGE_DIR / "repositories"

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".java",
    ".go",
    ".cpp",
    ".c",
    ".h",
    ".rs",
    ".php",
    ".rb",
    ".swift",
    ".kt",
    ".json",
    ".yaml",
    ".yml",
    ".md",
}