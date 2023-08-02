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
                "site" : "Ansa Economia",
                "link" : "https://www.ansa.it/sito/notizie/economia/economia.shtml",
                "rss" : "https://www.ansa.it/sito/notizie/economia/economia_rss.xml"
            },
            {
                "site" : "Market Watch",
                "link" : "https://www.marketwatch.com/",
                "rss" : "http://www.marketwatch.com/rss/topstories"
            }
        ]
    },
    # {
    #     "category" : "magazine",
    #     "feeds" : [
    #         {
    #             "site" : "Palladium",
    #             "link" : "https://www.palladiummag.com/",
    #             "rss" : "https://www.palladiummag.com/feed"
    #         }
    #     ]
    # },
    {
        "category" : "sardegna",
        "feeds" : [
            {
                "site" : "Ansa Sardegna",
                "link" : "https://www.ansa.it/sardegna",
                "rss" : "https://www.ansa.it/sardegna/notizie/sardegna_rss.xml"
            }
        ]
    },
    {
        "category" : "science",
        "feeds" : [
            {
                "site" : "Live Science",
                "link" : "https://www.livescience.com/",
                "rss" : "https://www.livescience.com/feeds/all"
            },
            {
                "site" : "New Scientist",
                "link" : "https://www.newscientist.com/",
                "rss" : "https://www.newscientist.com/feed/home/"
            },
            {
                "site" : "Phys Org",
                "link" : "https://phys.org/",
                "rss" : "https://phys.org/rss-feed/"
            },
            {
                "site" : "Scientific American",
                "link" : "https://www.scientificamerican.com/",
                "rss" : "http://rss.sciam.com/ScientificAmerican-Global"
            },
            {
                "site" : "Science News",
                "link" : "https://www.sciencenews.org/","rss" : "https://www.sciencenews.org/feed/"
            }
        ]
    },
    {
        "category" : "tech",
        "feeds" : [
            {
                "site" : "Hacker News",
                "link" : "https://news.ycombinator.com/",
                "rss" : "https://news.ycombinator.com/rss"
            },
            {
                "site" : "Wired",
                "link" : "https://www.wired.com/",
                "rss" : "https://www.wired.com/feed/rss"
            }
        ]
    },
    {
        "category" : "world",
        "feeds" : [
            {
                "site" : "Ansa Cronaca",
                "link" : "https://www.ansa.it/sito/notizie/cronaca/cronaca.shtml",
                "rss" : "https://www.ansa.it/sito/notizie/cronaca/cronaca_rss.xml"
            },
            {
                "site" : "Ansa Politica",
                "link" : "https://www.ansa.it/sito/notizie/politica/politica.shtml",
                "rss" : "https://www.ansa.it/sito/notizie/politica/politica_rss.xml"
            },
            {
                "site" : "Ansa Mondo",
                "link" : "https://www.ansa.it/sito/notizie/mondo/mondo.shtml",
                "rss" : "https://www.ansa.it/sito/notizie/mondo/mondo_rss.xml"
            },
            {
                "site" : "The Guardian",
                "link" : "https://www.theguardian.com/international",
                "rss" : "http://feeds.arstechnica.com/arstechnica/index/"
            },
            {
                "site" : "The New York Times",
                "link" : "https://www.nytimes.com/international/",
                "rss" : "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
            },
            {
                "site" : "Wall Street Journal",
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

    for item in feedsJson:
        fileName = "Sections/" + item["category"] + ".tex"
        with open(fileName, "w", encoding='utf-8') as f:
            for link in item["feeds"]:
                subSectionName = link["site"]
                subSectionLink = link["link"]
                subSection = "\\subsection{" + subSectionName + " \\href{" + subSectionLink + "}{\ding{225}}}\n"
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
                    newsTitle = "\\subsubsection{" + titleFormat +" \\href{" + n["link"] + "}{\ding{225}}}\n"
                    paragraph = summaryFormat + "\n"
                    data = "\\textit{" + data + "}\n\n"
                    f.write(newsTitle)
                    f.write(data)
                    f.write(paragraph)
        f.close()