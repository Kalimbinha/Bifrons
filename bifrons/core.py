import os


class Bifrons:
    def execute(self, title: str):
        current = self._read_version()
        current = self._normalize_version(current)

        level = self._classify(title)
        newv = self._increment(current, level)

        self._write_version(newv)

        print(f"[bifrons] versão anterior: {current}")
        print(f"[bifrons] nova versão: {newv}")

        return newv

    def _normalize_version(self, v: str) -> str:
        v = v.strip()
        if v.startswith("v"):
            v = v[1:]
        parts = v.split(".")
        while len(parts) < 3:
            parts.append("0")
        try:
            major, minor, patch = map(int, parts[:3])
        except ValueError:
            major, minor, patch = 0, 0, 0
        return f"{major}.{minor}.{patch}"

    def _classify(self, title: str):
        title = (title or "").lower().strip()

        if title.startswith(("fix", "bug", "hotfix", "patch", "bugfix", "error", "issue", "defect", "repair", "resolve")):
            return "patch"

        if title.startswith(("feat", "feature", "enhancement", "improvement", "minor", "add", "new", "implement", "introduce")):
            return "minor"

        if title.startswith(("breaking", "major", "release", "upgrade", "update")):
            return "major"

        raise ValueError("Título inválido! Use fix/feat/major")

    def _increment(self, version: str, level: str) -> str:
        major, minor, patch = map(int, version.split("."))

        if level == "patch":
            patch += 1
        elif level == "minor":
            minor += 1
            patch = 0
        elif level == "major":
            major += 1
            minor = 0
            patch = 0

        return f"{major}.{minor}.{patch}"

    def _read_version(self):
        if not os.path.exists("version.txt"):
            with open("version.txt", "w") as f:
                f.write("0.0.0")
            print("[bifrons] versão inicial criada: 0.0.0")
            return "0.0.0"

        with open("version.txt") as f:
            return f.read().strip()

    def _write_version(self, version: str):
        with open("version.txt", "w") as f:
            f.write(version)

