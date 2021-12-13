import wikipedia

def get_wikipedia_page(title):
    try:
        page = wikipedia.page(title)
    except Exception:
        return None
    return page

def get_max_word_page_and_count(titles):
    max_words_count = -1
    max_words_title = ""

    for title in titles:
        page = get_wikipedia_page(title)
        if page == None:
            continue
        count = len(page.summary.split())

        if count >= max_words_count:
            max_words_count = count
            max_words_title = page.title

    return (max_words_count, max_words_title)

def get_links_path(titles):
    path = [titles[0]]

    for i in range(len(titles) - 1):
        page = get_wikipedia_page(titles[i])
        if page == None:
            continue
        links = page.links

        if titles[i + 1] in links:
            path.append(titles[i + 1])
        else:
            for link in links:
                link_page = get_wikipedia_page(link)
                if link_page == None:
                    continue
                if titles[i + 1] in link_page.links:
                    path.append(link)
                    path.append(titles[i + 1])
                    break
    return path

data = input().split(", ")
titles = data[0:-1]
lang = data[-1]

if lang in wikipedia.languages().keys():
    wikipedia.set_lang(lang)
    max_word_info = get_max_word_page_and_count(titles)

    print(max_word_info[0], max_word_info[1])
    print(get_links_path(titles))

else:
    print("no results")
