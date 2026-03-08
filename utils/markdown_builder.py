def build_markdown_report(sector, news_data, analysis):

    report = f"# Trade Opportunity Report – {sector.title()} Sector\n\n"

    report += "## Recent Market Information\n\n"

    for item in news_data:
        report += f"- **{item['title']}**\n"
        report += f"  - {item['description']}\n"
        report += f"  - Source: {item['link']}\n\n"

    report += "## AI Market Analysis\n\n"
    report += analysis

    return report