import asyncio
from sqlalchemy.exc import OperationalError
from db.models import Base
from db.database import engine


async def init_models():
    print("⏳ Waiting for database to be ready...")

    for i in range(10):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            print("✅ Database initialized!")

            # ✅ Dispose engine cleanly
            await engine.dispose()
            return
        except OperationalError:
            print(f"Attempt {i+1}: DB not ready, retrying in 2s...")
            await asyncio.sleep(2)

    print("❌ Failed to connect to the database after 10 tries.")
    raise SystemExit(1)


if __name__ == "__main__":
    asyncio.run(init_models())
