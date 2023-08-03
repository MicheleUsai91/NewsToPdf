import feedparser
import ssl
from datetime import date

today = date.today()
date = today.strftime("%d-%b-%Y")

feedsJson = [
    {
        "category" : "economy",
        "feeds" : [
            {
                "site" : "ansa economia",
                "link" : "https://www.ansa.it/sito/notizie/economia/economia.shtml",
                "rss" : "https://www.ansa.it/sito/notizie/economia/economia_rss.xml"
            },
            {
                "site" : "market watch",
                "link" : "https://www.marketwatch.com/",
                "rss" : "http://www.marketwatch.com/rss/topstories"
            }
        ]
    },
    # {
    #     "category" : "magazine",
    #     "feeds" : [
    #         {
    #             "site" : "palladium",
    #             "link" : "https://www.palladiummag.com/",
    #             "rss" : "https://www.palladiummag.com/feed"
    #         }
    #     ]
    # },
    {
        "category" : "sardegna",
        "feeds" : [
            {
                "site" : "ansa sardegna",
                "link" : "https://www.ansa.it/sardegna",
                "rss" : "https://www.ansa.it/sardegna/notizie/sardegna_rss.xml"
            }
        ]
    },
    {
        "category" : "science",
        "feeds" : [
            {
                "site" : "live science",
                "link" : "https://www.livescience.com/",
                "rss" : "https://www.livescience.com/feeds/all"
            },
            {
                "site" : "new scientist",
                "link" : "https://www.newscientist.com/",
                "rss" : "https://www.newscientist.com/feed/home/"
            },
            {
                "site" : "phys org",
                "link" : "https://phys.org/",
                "rss" : "https://phys.org/rss-feed/"
            },
            {
                "site" : "scientific american",
                "link" : "https://www.scientificamerican.com/",
                "rss" : "http://rss.sciam.com/ScientificAmerican-Global"
            },
            {
                "site" : "science news",
                "link" : "https://www.sciencenews.org/","rss" : "https://www.sciencenews.org/feed/"
            }
        ]
    },
    {
        "category" : "tech",
        "feeds" : [
            {
                "site" : "hacker news",
                "link" : "https://news.ycombinator.com/",
                "rss" : "https://news.ycombinator.com/rss"
            },
            {
                "site" : "wired",
                "link" : "https://www.wired.com/",
                "rss" : "https://www.wired.com/feed/rss"
            }
        ]
    },
    {
        "category" : "world",
        "feeds" : [
            {
                "site" : "ansa cronaca",
                "link" : "https://www.ansa.it/sito/notizie/cronaca/cronaca.shtml",
                "rss" : "https://www.ansa.it/sito/notizie/cronaca/cronaca_rss.xml"
            },
            {
                "site" : "ansa politica",
                "link" : "https://www.ansa.it/sito/notizie/politica/politica.shtml",
                "rss" : "https://www.ansa.it/sito/notizie/politica/politica_rss.xml"
            },
            {
                "site" : "ansa mondo",
                "link" : "https://www.ansa.it/sito/notizie/mondo/mondo.shtml",
                "rss" : "https://www.ansa.it/sito/notizie/mondo/mondo_rss.xml"
            },
            {
                "site" : "the guardian",
                "link" : "https://www.theguardian.com/international",
                "rss" : "http://feeds.arstechnica.com/arstechnica/index/"
            },
            {
                "site" : "the new york times",
                "link" : "https://www.nytimes.com/international/",
                "rss" : "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
            },
            {
                "site" : "wall street journal",
                "link" : "https://www.wsj.com/",
                "rss" : "https://feeds.a.dj.com/rss/RSSWorldNews.xml"
            }
        ]
    }
]

specialCharacter = [
    {"char" : "à", "alt" : "\\`{a}"},
    {"char" : "è", "alt" : "\\`{e}"},
    {"char" : "ì", "alt" : "\\`{i}"},
    {"char" : "ò", "alt" : "\\`{o}"},
    {"char" : "ù", "alt" : "\\`{u}"},
    {"char" : "%", "alt" : "\\%"},
    {"char" : "$", "alt" : "\\$"},
    {"char" : "°", "alt" : "\\ang"},
    {"char" : "<p>", "alt" : ""},
    {"char" : "</p>", "alt" : ""},
    {"char" : "<a>", "alt" : ""},
    {"char" : "</a>", "alt" : ""},
    {"char" : "&nbsp;", "alt" : ""},
    {"char" : "#", "alt" : ""},
    {"char" : "&", "alt" : "\\&"},
]

if hasattr(ssl, "_create_unverified_context"):
    ssl._create_default_https_context = ssl._create_unverified_context

    with open("News.md", "w", encoding='utf-8') as f:
        toc = "# Table of Content\n"
        f.write(toc)
        i = 1
        for item in feedsJson:
            category = item["category"]
            catItem = str(i) + ". [" + category.capitalize() + "](#" + category + ")\n"
            i += 1
            f.write(catItem)
            j = 1
            for link in item["feeds"]:
                subCategory = link["site"]
                subCategoryLink = subCategory.replace(" ", "-")
                subCatItem = "\t" + str(j) + ". [" + subCategory.capitalize() + "](#" + subCategoryLink + ")\n"
                j += 1
                f.write(subCatItem)
        
        f.write("\n")
        
        for item in feedsJson:
            sectionTitle = item["category"]
            section = "# " + sectionTitle.capitalize() + "\n"
            print(section)
            f.write(section)
            for link in item["feeds"]:
                subSectionName = link["site"]
                subSectionLink = link["link"]
                subSection = "## *[" + subSectionName.capitalize() + "](" + subSectionLink + ")*\n"
                print(subSection)
                f.write(subSection)
                feed = feedparser.parse(link["rss"])
                for n in feed["items"]:
                    title = n["title"]
                    summary = n["summary"]
                    dataArr = n["published"].split(" ")

                    titleFormat = title
                    summaryFormat = summary
                    data = dataArr[1] + "-" + dataArr[2] + "-" + dataArr[3]
                    for c in specialCharacter:
                        char = c["char"]
                        alt = c["alt"]
                        if char in title:
                            titleFormat = titleFormat.replace(char, alt)
                        if char in summary:
                            summaryFormat = summaryFormat.replace(char, alt)
                    newsTitle = "### *[" + titleFormat + "](" + n["link"] + ")*\n"
                    paragraph = summaryFormat + "\n"
                    data = "_" + data + "_\n\n"
                    f.write(newsTitle)
                    f.write(data)
                    f.write(paragraph)
                    f.write("\n---\n")
        f.close()