import xml.etree.ElementTree as ET
from datetime import datetime


def generate_sitemap(urls):
    urlset = ET.Element(
        "urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for loc, lastmod, changefreq, priority in urls:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = loc
        ET.SubElement(url, "lastmod").text = lastmod
        ET.SubElement(url, "changefreq").text = changefreq
        ET.SubElement(url, "priority").text = str(priority)

    tree = ET.ElementTree(urlset)
    tree.write("sitemap.xml", encoding="UTF-8", xml_declaration=True)


# Example usage
urls = [
    ("https://gamerasnap.li2niu.com/",
     datetime.now().strftime("%Y-%m-%d"), "weekly", 1.0),
    ("https://gamerasnap.li2niu.com/changelog",
     datetime.now().strftime("%Y-%m-%d"), "monthly", 0.8),
    ("https://gamerasnap.li2niu.com/privacypolicy",
     datetime.now().strftime("%Y-%m-%d"), "monthly", 0.8),
    ("https://gamerasnap.li2niu.com/privacypolicy-cn",
     datetime.now().strftime("%Y-%m-%d"), "monthly", 0.8),
    ("https://gamerasnap.li2niu.com/support",
     datetime.now().strftime("%Y-%m-%d"), "monthly", 0.8),
    ("https://gamerasnap.li2niu.com/support_cn",
     datetime.now().strftime("%Y-%m-%d"), "monthly", 0.8),
    ("https://gamerasnap.li2niu.com/tutorial",
     datetime.now().strftime("%Y-%m-%d"), "monthly", 0.8),
    ("https://gamerasnap.li2niu.com/tutorial-cn",
     datetime.now().strftime("%Y-%m-%d"), "monthly", 0.8),
]

generate_sitemap(urls)
