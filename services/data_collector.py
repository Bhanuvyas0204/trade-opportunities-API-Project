from ddgs import DDGS

def get_sector_news(sector: str):

    query = f"{sector} industry India market news"

    results = []

    with DDGS() as ddgs:
        news = ddgs.text(query, max_results=5)

        for item in news:
            results.append({
                "title": item.get("title"),
                "description": item.get("body"),
                "link": item.get("href")
            })

    return results