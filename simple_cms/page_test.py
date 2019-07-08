import math


def get_page_range(page_num, show_num, current_page):
    # 分偶数和奇数
    current_page = int(current_page)
    page_num = int(page_num)
    show_num = int(show_num)

    if show_num % 2 == 0:
        fore = int((show_num - 1) / 2)
        after = int(show_num / 2)
    else:
        fore = int(show_num / 2)
        after = math.ceil((show_num - 1) / 2)

    star = current_page - fore
    end = current_page + after
    if star < 1:
        if star == 0:
            star = 1
        end += int(math.fabs(star))
        star = 1

    if end > page_num:
        star -= end - page_num
        end = page_num

    if star < 1:
        star = 1
    if end > page_num:
        end = page_num
    return star, end


print(get_page_range(1000, 5, 3))
