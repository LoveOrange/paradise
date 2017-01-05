# paradise
---

## 简介
Paradise是一款基于配置文件的自动化测试框架，支持对页面元素（DOM）和API进行测试。

## 快速上手
### 1. 环境准备
Paradise对于页面元素的测试基于Selenium，使用页面元素测试前，请保证系统中已经安装了Selenium，如果没有安装，请尝试使用以下命令安装：

> pip install selenium

并且将所需要测试浏览器驱动，加到环境变量中（参考：）。

### 2. 配置文件
Paradise中使用两种配置文件对cases进行管理：
1. **config.yml**
一个config.yml的例子：
```
host: https://baidu.com

selenium:
    type: chrome

case_files:
  - api: "cases/api.yml"
  - dom: "cases/dom.yml"
```

config.yml包含三种标签：

- host：用于配置测试URL的基本路径，需要以http:// 或 https:// 开头
* selenium.type: 配置测试使用的浏览器，目前仅支持chrome
* case_files: 配置用于保存测试用例的配置文件。配置文件分为两种，分别用于存放页面元素的测试和API的测试，对应key分别为dom和api，value为具体文件的路径。case_file如何编写，见下文。

2. **case.yml**

一个dom-case-file.yml的例子：
```
- check_title:
    url: "https://baidu.com"
    actions:
      - scripts: "sh shell/ci.sh"
      - fill: ".s_ipt(LoveOrange)"
      - sleep: 1
      - click: ".s_btn"
      - sleep: 1
    validate: "title"
    expect:
      - equals: "LoveOrange_百度搜索"
```

- check_title：用户可自定义，为当前测试case的名字
* url：可选参数，指定测试页面的url，如果不填，则为全局默认的url
* actions：动作流，用于指定对页面的一些操作。示例中动作流执行的动作为：执行`sh shell/ci.sh`命令，找到url为`https://baidu.com`页面**class**为`s_ipt`的页面元素，并填充值`LoveOrange`，等待1s，点击**class**为`s_btn`的页面元素，等待1s。具体动作流配置方法，参见下文**动作流**
* validate：带验证的页面元素
* expect：预期的结果，目前仅支持equals

一个api-case-file.yml的例子：
```
- is_ok:
    url: /ok
    method: get
    headers:
      - header1: header_value
    params:
      - param1: param_value
    expect:
      - equals: "ok"
```

- is_ok：用户可自定义，为当前测试case的名字
* url：可选参数，指定测试页面的url，如果不填，则为全局默认的url
* method：调用api所使用的http方法，目前支持get和post
* headers：调用api所使用的headers参数，本例中，headers中有一个参数，key为header1，value为header_value
* params：调用api所使用的参数，本例中，有一个参数，key为param1，value为param_value
* expect：预期的结果，目前仅支持equals

3. **工作流**
*目前只有针对页面元素的测试可以使用工作流*
工作流的格式如下：
```
actions:
  - ${action_type}: ${action_value}
```
目前支持的action_type有：
- scripts：执行一个shell命令，参数为字符串，
* sleep：等待一定时间，参数为数字，单位s
* fill：对某一页面元素填充数据，使用case file的DSL，如何编写请参考下文**Case File DSL**
* click：点击某一页面元素，使用case file的DSL

配置的工作流，会在执行当前测试时**优先**执行，然后再去验证此case的结果

4. **Case File DSL**
由于yml文件value的限制，为了实现页面元素的选择，填充，Paradise定义了一个迷你的DSL，用于实现上述操作。

以上文的配置文件举例：
```
actions:
      - fill: ".s_ipt(LoveOrange)"
      - click: ".s_btn"
```

此例中，fill动作的参数为`.s_ipt(LoveOrange)`，其中，`.s_ipt`用户dom的选择，类似于经典的jQuery，`.s_ipt`表示选择class值为s_ipt的元素，类似的，`#s_ipt`可以用于选择id值为s_ipt的元素。后半部分的`(LoveOrange)`，表示对于所选择的元素，填充的值为“LoveOrange”，使用括号包含起来，表示这是fill动作的参数。对于另一个动作click来说，click不需要参数，click动作的参数为`.s_btn`



## 重要提示：
Paradise仍然是一个开发中的框架，目前部分功能尚未实现（Case File DSL，API Test。api功能跟pyresttest略有重合，暂时延缓开发）。目前仍未Beta版本，仅供演示使用，第一个可用版本预计在圣诞节前放出

