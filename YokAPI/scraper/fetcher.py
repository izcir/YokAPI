import aiohttp
import asyncio
import certifi
import ssl

class Fetcher:
    def __init__(self, session: aiohttp.ClientSession = None):
        self.session = session
        self.BASE_URL = "https://yokatlas.yok.gov.tr"
        self._bool_session = session is None

    async def __aenter__(self):
        if self.session is None:
            self.session = await self._create_session()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self._bool_session and self.session:
            await self.session.close()

    def _get_headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
        }

    async def _create_session(self):
        # ssl_context = ssl.create_default_context(cafile=certifi.where())
        return aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False),
            headers=self._get_headers()
        )

    async def year_control(self, year: int) -> str:
        available_years = [2022, 2023, 2024] # eski yıllar kaldırıldı -> [2019, 2020, 2021, 2022, 2023, 2024]
        year = int(year)

        if year not in available_years:
            raise ValueError(f"Geçersiz değer: {year}. Yıl sadece {available_years} yıllarından biri olabilir.")
        
        return "" if year == 2024 else f"{year}/"

    def return_url(self, year_path: str, end_url: str) -> str:
        return f"{self.BASE_URL}/{year_path}{end_url}"

    async def fetch(self, url: str) -> str:
        if self.session is None:
            self.session = await self._create_session()
            self._bool_session = True

        async with self.session.get(url) as response:
            return await response.text()

    async def send_request(self, year: int, endpoint: str) -> str:
        year_path = await self.year_control(year)
        url = self.return_url(year_path, endpoint)
        return await self.fetch(url)

    async def close(self):
        if self._bool_session and self.session:
            await self.session.close()
            self.session = None
