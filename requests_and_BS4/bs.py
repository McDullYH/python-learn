# 强烈建议使用lxml 和 html5lib做解析
# BS4 就是调用他们进行解析的

# bs 将HTML转换成树，每个节点可以是 Tag NavigableString BeautifuleSoup Comment

# Tag最重要的属性 name （一个） 和 attributes（多个） 多值属性返回list


# NavigableString 就是 tag 夹住的字符串
tag.string

# contents 就是 tag夹住的所有的内容
tag.contents
# contents[n] 表示tag夹住的第n+1个tag的内容
tag.contents[n]
# 返回子节点个数
len(tag.contents)
# 如果一个tag没有子tag或者只有字符串，那么调用contents会出错

# tag 的子节点生成器
for child in tag.children:
    pass

# tag 的子孙节点
for child in tag.descendants:
    pass
# 即深度优先遍历子节点和所有子孙节点

# 如果一个tag的唯一子tag只有一个字符串 那么可以直接使用.string
tag.string

# 使用replace_with方法替换
tag.string.replace_with('string')

# tag的多个字符串可以通过strings获取
tag.strings
tag.stripped_strings    #去除多余空白

# 获取title的父节点
tag.parent
# 字符串也有父节点，下例中也就是tag
tag.string.parent
# 顶层节点的父节点是 BeautifulSoup对象
# BeautifulSoup的父节点是None

# parents 方法可以便利所有父，祖先节点 先是父亲，后是祖先(最后必然是None)


# 兄弟节点
tag.next_sibling
tag.previous_sibling
# 注意兄弟可能是换行符，即不是一个tag，
# 所有兄弟
tag.next_siblings
tag.previous_siblings

# 回退和前进
tag.next_element
tag.previous_element
tag.next_elements
tag.previous_elements

# Comment是NavigableString的子类

# BeautifulSoup类型表示一个文档的全部内容，他不是tag，但包含一个name属性，值都是是"[document]"
soup.name

# 获取第一个 <a> tag
soup.a

# 获取所有的 <a>
soup.find_all('a')
# 可以使用正则表达式
import re
find_all(re.compile("^b"))  #匹配 <b> 和 <body> 感觉实际似乎用处不大
# 可以一次匹配多个
find_all(["a","b"])
# 不同于下面的，下面的是返回class为title 的 p标签
find_all("p","title")
# 匹配任意值
find_all(True)

# 所以 搜索的参数可以是 字符串，列表，正则表达式，True

# 自定义方法
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
find_all(has_class_but_no_id)

def surrouded_by_strings(tag):
    return (isinstance(tag.next_element,NavigabelString)) and (isinstance(tag.previous_element,NavigableString))
find_all(surrounded_by_strings)

# 深入 file_all
# 按照keyword参数搜索
# 搜索的参数依然可以是 字符串，列表，正则表达式，True 后面不再说明
tag.find_all(id='value')
tag.find_all(href=re.compile("elsie"), id='link1')
# 有些属性不能使用，如data-*
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(data-foo="value")
# SyntaxError: keyword can't be an expression
# 但是可以像下面这样
data_soup.find_all(attrs={"data-foo": "value"})

# 搜索class
tag.find_all("a",class_="value")
# 搜索文本
tag.find_all("a",text="Elsie")
tag.find_all("a",text=["Elsie","Tille"])
# 上面是返回tag，下面是返回文本
tag.find_all(text="Elsie")

# limit
tag.find_all("a",limit=2)

# recursive 如果只搜索直接子节点
tag.find_all("a",recursive=False)

# 由于find 方法用的最多，所以可以简写
tag.find_all("a",recursive=False)
tag("a",recursive=False)
# 这2个是一样的

# 同理，find方法也可以简写
soup.find("head").find("title")
soup.head.title
# 在麦酷记事里面搜索Chain，会的到启发

# 其他的find方法
find_parents( name , attrs , recursive , text , **kwargs )
find_parent( name , attrs , recursive , text , **kwargs )
find_***_siblings( name , attrs , recursive , text , **kwargs )
find_***_sibling( name , attrs , recursive , text , **kwargs )
find_all_next
find_next
find_all_previous
find_previous
# 上面4个就是和element对应的


# ****还支持CSS选择器查找****，使用select方法
# 看CSS选择器就知道怎么操作了



# 后面的内容是修改文档树了，暂时用不上
# 只有一个需要提到的方法 extract() 把tag从当前文档树移除，并返回


# Beautiful Soup解析之后，文档都变成了Unicode
# Beautiful Soup一律输出UTF-8

# SoupStrainer 可以指定仅仅解析部分内容

# 调试方法 使用 diagnose可以知道 BS是怎么处理一份文档的
form bs4.diagnose import diagnose



# prettify()方法可以漂亮的输出
