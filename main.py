import asyncio

from parser import IdeasParser


async def main() -> None:
    """Запуск парсера."""
    ip = IdeasParser()
    await ip.init()

    try:
        await ip.get_ideas()
    finally:
        ip.save()
        await ip.session.close()


if __name__ == "__main__":
    asyncio.run(main())
