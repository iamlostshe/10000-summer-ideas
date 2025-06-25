import asyncio
import json
from pathlib import Path

from aiohttp import ClientSession

URL = "https://xn--80aqu.xn--e1alkp.xn--90acagbhgpca7c8c7f.xn--p1ai/"
CATEGORIES = (
    "646f5e533903e748c2603826",
    "646f5e4a3903e748c2603825",
    "646f5e3b3903e748c2603824",
    "646f5e333903e748c2603823",
    "646f5e2c3903e748c2603822",
    "646f5e243903e748c2603821",
    "646f5e1a3903e748c2603820",
    "646f5e133903e748c260381f",
    "646f5e0c3903e748c260381e",
    "646f5e053903e748c260381d",
    "646f5dfb3903e748c260381c",
    "646f5df43903e748c260381b",
    "646f5def3903e748c260381a",
    "646f5de93903e748c2603819",
    "646f5de33903e748c2603818",
    "646f5dde3903e748c2603817",
    "646f5dd63903e748c2603816",
    "646f5dce3903e748c2603815",
    "646f5dc73903e748c2603814",
    "646f5dc13903e748c2603813",
    "646f5dba3903e748c2603812",
    "646f5daf3903e748c2603811",
    "646f5ce73903e748c2603810",
)


class IdeasParser:
    """Класс парсера идей."""

    async def init(self) -> None:
        """Инициализация сессии."""
        self.res = []
        self.session = ClientSession(base_url=URL)

    async def fetch_ideas(self, category: str) -> dict:
        """Получить идеи для одной категории."""
        async with self.session.get(f"ideas?c={category}") as r:
            data = json.loads(await r.text()).get("ideas", [])
            return self.res.extend(data)

    async def get_ideas(self) -> list[dict]:
        """Получить все идеи."""
        tasks = [self.fetch_ideas(c) for c in CATEGORIES]
        await asyncio.gather(*tasks)

    def save(self) -> None:
        """Сохранение массива идей."""
        with Path("index.json").open("w+", encoding="utf-8") as f:
            json.dump(
                sorted(self.res, key=lambda x: int(x["number"])),
                f,
                ensure_ascii=False,
                indent=4,
            )

        print(f"В базу записано {len(self.res)} идей!")
