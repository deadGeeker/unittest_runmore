### 前言
本次项目使用unittest来完成多自动化脚本的执行
  
##### 分析  
1. 目录结构  
--unittest  
&nbsp;&nbsp;|--runtests.py  
&nbsp;&nbsp;|--report  
&nbsp;&nbsp;&nbsp;&nbsp;|—-report.html  
&nbsp;&nbsp;|--tests   
&nbsp;&nbsp;&nbsp;&nbsp;|--test1.py   
&nbsp;&nbsp;&nbsp;&nbsp;|--test2.py   
&nbsp;&nbsp;&nbsp;&nbsp;|--__init__.py   
  
2. 功能剖析  
通过执行runtests.py来执行tests文件夹下的全部test*.py脚本，然后用HTMLtestrunner输出测试报告


##### 代码实现  
1. 引入unittest模块  

2. 编写test1和test2脚本，注意：__init__脚本为空，主要是让tests看起来是包  
 
3. 编写runtests脚本  

4. 使用HTMLTestRunnner生成测试报告  
+ 下载HTMLTestRunnner.py (https://pypi.org/project/HTMLTestRunner/)  
+ 复制到python三方目录下的当中 (..\Python\Python38\Lib\site-packages)  
+ 官网的是python2语法写的，手动把官网的HTMLTestRunner.py改成python3的语法：  
  + 第94行，将import StringIO修改成import io  
  + 第539行，将self.outputBuffer = StringIO.StringIO()修改成self.outputBuffer = io.StringIO()  
  + 第631行，将print >> sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)修改成print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))  
  + 第642行，将if not rmap.has_key(cls):修改成if not cls in rmap:  
  + 第766行，将uo = o.decode('latin-1')修改成uo = e  
  + 第775行，将ue = e.decode('latin-1')修改成ue = e  

---
unittest自动化执行框架相关方法可以通过help()方法来查阅学习
