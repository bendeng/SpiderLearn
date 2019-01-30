from lxml import etree

html = """

<html>
    <body>
    <ul>
     <li>1
         <a href="ftwww">子1</a>
     </li>
     <li>2
        <a href="xxx">子2</a>
     </li>
     <li>3
        <a href="ftyyy">子3</a>
     </li>
     <li>4
         <a href="zzz">子4</a>
     </li>
     <li>5
        <a href="ftaaa">子5</a>
     </li>
     
 </ul>
 </body>
 </html>
"""

def xpath_parse():
    # 1.转解析类型
    xpath_data = etree.HTML(html)
    # 2.xpath 语法
    # -> 按节点路径搜索，使用/
    # -> 跨节点搜索，使用  //
    # -> 精确搜索，使用 //tag[@属性名="属性值"]
    # ->
    # ->
    result = xpath_data.xpath('/html/body/ul/li')   #搜索这个路径下的li标签  [<Element li at 0x10d17ab88>, <Element li at 0x10d17ab48>, <Element li at 0x10d17ac48>, <Element li at 0x10d17ac88>, <Element li at 0x10d17acc8>]
    result = xpath_data.xpath('//li')               #和上一条搜索方法一样，只是跨路径  [<Element li at 0x110e41d88>, <Element li at 0x110e41d48>, <Element li at 0x110e41e48>, <Element li at 0x110e41e88>, <Element li at 0x110e41ec8>]
    result = xpath_data.xpath('//a[@href="aaa"]')   #精确搜索    [<Element a at 0x107f0bdc8>]
    result = xpath_data.xpath('//a[@href="aaa"]/text()')  # 标签包裹的内容，使用text()  ['子5']
    result = xpath_data.xpath('//a/@href')          #获取标签的属性值   ['ftwww', 'xxx', 'ftyyy', 'zzz', 'ftaaa']
    #那么下面这句就很容易理解了，即获取li的值，返回一个list
    result = xpath_data.xpath('//li/text()')
    #xpath还可以这样，通过索引直接取多个'平级'的标签的某个标签
    result = xpath_data.xpath('//li[2]/text()')     #['子1', '子2', '子3', '子4', '子5']
    #虽然//a可以取出多个a，但是不能通过索引值去获取某一个a，因为a标签并不是平级的
    result = xpath_data.xpath('//a[2]/text()')      #[]

    #xpath还有模糊查询的功能
    result = xpath_data.xpath('//a[contains(@href,"ft")]/@href')  # ['ftwww', 'ftyyy', 'ftaaa']
    #下一个节点(平级关系)：following-sibling::*

    print(result)

xpath_parse()