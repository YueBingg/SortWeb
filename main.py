from baiduspider import BaiduSpider


def search_web(query, all_count):
    pn = 0
    flag = 1
    result = []
    page_count = 0
    spider = BaiduSpider()
    while flag:
        pn += 1
        web_result = spider.search_web(query=query, pn=pn, exclude=['all'])
        web_result = web_result['results']
        for i in range(1, len(web_result)):
            if 'des' not in web_result[i].keys() or web_result[i]['des'] is None: continue
            web_result[i]['count'] = web_result[i]['des'].count(query)
            result.append(web_result[i])
            print(str(page_count) + ': ' + str(web_result[i]['count']) + web_result[i]['des'])
            page_count += 1
            if page_count == all_count:
                flag = 0
                break
    return result


def sort_web(web_result):
    web_result.sort(key=lambda x: x['count'], reverse=True)
    return web_result


def print_sort_web(type):
    """
    'des': 简介
    'origin':来源网页
    'title': 标题
    'url': 百度地址
    :param type:输出类型
    :return:
    """
    for item in result:
        print(str(item['count']) + ': ' + item[type])


if __name__ == '__main__':
    all_count = 20
    query = "大学"
    result = search_web(query, all_count)
    result = sort_web(result)
    print_sort_web('url')
