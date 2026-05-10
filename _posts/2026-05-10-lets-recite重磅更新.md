---
title: lets-recite重磅更新
date: 2026-05-10 17:47
tags: [项目,党团]
categories: [文档]
---

## 关于项目

项目地址 <https://www.565455.xyz/projects/lets-recite/>

开源于Github <https://github.com/Fancc666/lets-recite>

辅助记忆小工具，可以用来背政治历史这类的背诵型学科，支持随机题目，题目全览和语音朗读功能。

## 更新内容

“一起背政治”项目正式更名“一起背吧”，通过重构现在我们有了更好的词书加载方式。

![Img](https://qnhdpic.twt.edu.cn/download/origin/fbec42374c6a121dff913e937b84a926.png)


您只需要在`/books`按照`README.md`上传标准词书，并在`books.js`中填写词书信息即可发起pr，您的词书合理的情况下我会100%merge。

欢迎提交pr新增词书或一起改进项目。

## 新词书

这是建工学院党建积极分子考试大纲的题库，可以参考它来构建新词书。

```js
{
    file: "jgdj.json",
    name: "建工积极分子@2026",
    description: "建工积极分子考试大纲"
}
```

```json
{
  "bookName": "天津大学建工学院党建学习资料",
  "data": [
    {
      "id": 1,
      "question": "入党誓词",
      "answer": "我志愿加入中国共产党，拥护党的纲领，遵守党的章程，履行党员义务，执行党的决定，严守党的纪律，保守党的秘密，对党忠诚，积极工作，为共产主义奋斗终身，随时准备为党和人民牺牲一切，永不叛党。"
    },
    {
      "id": 2,
      "question": "党章的地位",
      "answer": "党章是党的总章程，是党的根本大法。体现着党的十九大以来以习近平同志为核心的党中央在党的理论创新、实践创新、制度创新上的新成果，蕴含着对新时代新征程党和国家事业发展的新要求，党的二十大通过的党章为全党统一思想、凝聚力量迈向新征程提供了根本遵循。"
    }
  ]
}
```

效果展示

![Img](https://qnhdpic.twt.edu.cn/download/origin/b29dc26482ef448ee27d33df6b43de9e.png)

![Img](https://qnhdpic.twt.edu.cn/download/origin/837f38efa6ced90ed3b2554a0093476c.png)
