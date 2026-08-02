class AtlasLogger:
    """Simple console logger for Atlas."""

    def info(self, message: str):
        print(message)

    def success(self, message: str):
        print(f"✓ {message}")

    def header(self, message: str):
        print("=" * 50)
        print(message)
        print("=" * 50)

    def section(self, message: str):
        print(f"\n{message}\n")