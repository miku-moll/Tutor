# 版本历史

v1.0 2015/06/12

v1.1 2015/09/09 修改原有描述，增加设计阶段的术语说明

v1.2 2016/02/15 增加格式说明 

v2.0 2018/01/09 大量修订补充内容

v2.1 2018/03/08 增加形式审查说明

v2.2 2018/03/21 增加实现、测试的相关说明，其它小的修改

v2.3 2019/03/20 增加术语及缩略语的编写说明

v2.4 2020/10/20 新浪博客即将关停，将很多文章加密导致非作者无法访问，迁移到其它平台

# 零、前言
论文提交导师之前，请按照下面清单逐一检查。注意导师并不负责检查论文格式、错别字。

论文的格式一定不要出问题，也就是**形式审查必须要不出问题**。因为论文答辩前送交三位评阅专家盲审，论文格式不标准（字有大有小，图歪歪扭扭，错字别字多，页眉页脚错误等），会导致专家印象恶劣。专家懒得指出你的论文中细节的格式错误，但评阅书上又要求必须指出论文不足，专家就会提一些非常困难的问题。改不满意，专家在二审时仍然不给过。三审按照规则就要等待至少3个月。三审不过就没有答辩资格了。

a\) 所以，不要作。

b\) 请根据博文《硕士论文自查清单》（简称"自查"）逐一对照检查论文。
http://blog.sina.com.cn/s/blog\_686020310102vst4.html

c\)
如果专家的评阅意见上有"论文格式错误很多"这样的字样，再审不过的可能性骤增


论文范例：==\> [[【点击这里】]{.underline}](http://wenku.baidu.com/view/2729229551e79b896802266e.html) 
 （存放于百度文库中，免费下载。如果发现需要收费，请在本文下方留言，我将会换一个不收费的地方存放）

# 一、摘要

1.1 摘要采用了三段论吗？

1.2
英文摘要是采用机器翻译完成的吗？Google翻译仅做参考，要是你把Google翻译结果直接放上来，论文不会通过导师评审的！

1.3 英文摘要的标点是半角符号吗？

    【误】**It's** designed to\
    【正】**It\'s** designed to

1.4 关键词数量是4-6个吗？

1.5 关键词长度超过4个汉字吗？单个关键词请限制在4个汉字之内

1.6
关键词是非常常见的技术术语吗？（超过10年历史的术语）常见术语不要当做关键词

    【误】Java EE, 数据库\
    【正】反洗钱 深度学习

1.7 中文摘要另起一页了吗？英文摘要另起一页了吗？中英文摘要不能连在一页中

# 二、一般格式

2.1 论文模板是最新的？（\--\>http://sse.bupt.edu.cn/info/1064/2026.htm
右侧"**论文答辩及相关材料下载**"）

2.2 论文封面是"北京邮电大学 硕士学位论文"

2.3
章节编号是连续的吗？所有章节编号都需要顺序增长，不能跳着编。请在论文目录中检查

2.4
连续的两级标题之间有文字说明吗？在上级标题之后必须有文字说明（一般是对本节文字的总体简要介绍），不可以直接接下级标题

2.5 章节编号采用的是半角字符吗？注意不能用全角符号

2.6
整个论文的小节内的编号是一致的吗？有没有混乱的编号，比如上一个小节用ABC，下一个小节用123，另一个小节用圆点儿

2.7
每一章的章标题都是从新一页的顶部开始的吗？不要将新的一章标题和上一章的末尾文字放在一页

2.8
论文图片是你自己亲手绘制的吗？如果是网上粘贴的，请你亲手再绘制一遍（建议用visio）

2.9
图片打印后清晰否？如果能够看出明显的锯齿或者马赛克，那么图片需要重新绘制或者截取。

2.10
图片最好不要背景色。因为深背景色图片打印后，看上去黑乎乎一片，很难分辨图片细节

2.11
图片中的文字不大于正文文字，文字宽高比例要保持正常，不能随便拉伸图片

2.12 图的题注位于图的下方居中

2.13 图的题注中包含章节编号以及章节内编号，比如 "图 5-2 总体结构图"

2.14
图片在页面居中放置，左右空白对称。不可以是"正文缩进"再居中（正文缩进居中，图片会偏右）

2.15 图的长度和宽度不超过页面的文字边距

2.16
图片中不含有大片空白。如果有大片空白，则需将图片空白裁掉之后方能贴入论文（Word中自带图片裁剪功能）

2.17
图片是采用"嵌入式"的样式放入正文的吗？不要用其他样式（紧密型、上下型等）

2.18 表格是用word中的表格绘制的，不能弄张图片贴进去

2.19 表格的题注在表格上方居中。（图的题注位于图片下方）

2.20 表格的题注中包含章节编号以及章节内编号。\
    【误】 表 1  性能分析\
    【正】 表3-2 加密算法参数

2.21 图和表的题注全部都用楷体。

2.22
论文中所有表的样式须保持一致。表格样式不能变化多端，比如有的用虚线框，有的用实线框。

2.23
论文的正文部分：奇数页页眉应为章节名，偶数页页眉是"北京邮电大学硕士学位论文"

2.24 "参考文献"和"致谢"不应做章节编号

2.25
矢量图（比如Visio绘制的图）转换为jpg/png等标量图时，分辨率不低于200dpi，保证打印后的质量

# 三、参考文献

3.1 论文的参考文献数量不少于15个，参考文献中应有1/3是最近3年的新文献

3.2 正文后面的"参考文献"的格式必须要符合"中华人民共和国国家标准GB/T
7714-2005"的要求（[[http://wenku.baidu.com/view/46677c4ecf84b9d528ea7a80.html]{.underline}](http://wenku.baidu.com/view/46677c4ecf84b9d528ea7a80.html)）。

3.3 所有列于"参考文献"章节中的文献，均在正文中进行了引用

3.4 参考文献被引用时，文献编号的字体设置为"上标"\
【正】在维系并稳定企业客户的同时又扩大客户群，最终实现企业经济效益的提升**^\[1\]^**。

参考文献

\[1\] CRM. http://baike.baidu.com/view/648655.htm.

# 四、绪论

4.1 【本人承担任务】小节用列表形式列出自己在项目中所做的主要任务

4.2  课题背景中没有为领导歌功颂德的句子和词汇

# 五、相关技术

5.1  不可作为相关技术的内容：Android、C++、Java
(EE)、一般数据库（MySQL、Oracle、MS SQL Server等）、HTML、面向对象技术

# 六、需求分析

6.1 有总体功能需求描述 （使用一张用例图）

6.2 各个功能需求有对应的用例规约表

6.3 使用用例图描述参与者和功能需求间的关系

6.4 有非功能性需求的描述（例如性能需求、可靠性需求、安全性需求等）

6.5 用例图中的所有线条都带有箭头

6.6
用例图中的一般关联关系用实线箭头"\-\-\-\-\-\--\>"，不是实心/空心三角箭头

6.7 用例图中的"包含"关系使用虚线箭头

6.8 用例的名字必须都是"动宾短语"，不准使用名词短语

6.9
在需求分析章节中不能使用"模块"这样的术语。"模块"是设计阶段才有的概念！

# 七、设计阶段

7.1
在概要设计和详细设计章节中，不能在标题中再出现"功能"的字样。例如不能用"功能1概要设计"、"登录功能详细设计"；而改为"模块1概要设计"、"XXX模块详细设计"、"XXX子系统概要设计"

7.2
绘制流程图时，应按照软件工程规范要求，"开始"和"结束"采用相应的图形符号

# 八、实现阶段

8.1
实现阶段可以有实际系统运行时的截图。但是截图一般不超过5张，除非你有特别的理由

8.2
实现阶段一般不能在论文中粘贴代码，除非是特别关键的算法。否则一般使用流程图或者伪代码

# 九、部署测试

9.1 测试部分要给出4个以上的测试用例以及对应的测试结果

9.2 如果论文没有实现部分，那么在部署测试章节要给出**系统运行的截图**以证明该系统是一个实际而非伪造的系统。

# 十、致谢

10.1
如果是在导师项目组的全日制硕士，针对导师，可以只写一句："感谢xxx老师指导本人完成学习研究以及论文工作"；或者不写。

10.2
如果是非全日制工程硕士，针对导师，只写一句："感谢XXX老师指导本人论文写作"；或者不屑

10.3
不准夸张。不准用"热爱"、"衷心"等表示强烈情感的词汇来描述导师；也不准说你从导师身上学到了xx（你学到了好的就肯定学到了坏的）；更不准说导师影响了你的人生（研究生学习满打满算3年时间，导师怎么可能影响你的人生？）

# 十一、行文规范

01\.
专业术语，包括英文缩写要在第一次出现时给出全文和翻译。如果在摘要中不便于说明，那么在正文中第一次出现时给出。样式如下

  a) 英文缩写（英文全文，中文翻译），例如：MQ (Message Queue, 消息队列) 

  b) 中文术语（英文缩写，英文全文），例如：客户机/服务器（C/S, Client/
Server）

  c) 英文术语（英文缩写，中文翻译），例如：Delegating Constructor （dele
ctor，代理构造函数）