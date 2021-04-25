### 前言
本次项目使用unittest来完成多自动化脚本的执行
  
##### 分析  
1. 目录结构
--unittest  
 |-runtests.py  
 |-tests  
  |-test1.py  
  |-test2.py  
  |-__init__.py  
  
2. 功能剖析  
通过执行runtests.py来执行tests文件夹下的全部test*.py脚本


##### 代码实现  
1. 引入unittest模块
  

2. 编写test1和test2脚本，注意：__init__脚本为空，主要是让tests看起来是包
 
   
3. 编写runtests脚本
  
---
unittest自动化执行框架相关方法可以通过help()方法来查阅学习
