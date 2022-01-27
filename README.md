# tokyocovid19crawler

Use Python to web crawling Tokyo covid-19 website information into csv file and send Email automatically.

[東京都 新型コロナウイルス感染症対策サイト](https://stopcovid19.metro.tokyo.lg.jp/zh-tw/)

### Requirement

Check your chrome version to install the right [ChromeDriver](http://chromedriver.chromium.org/) version
Put ChromeDriver into ```usr/local/bin```

```
$ pip3 install lxml 
$ pip3 install selenium 
$ pip3 install pandas 
```

### Run
```
python webcrawler.py
python sendemail.py
```


### Input email and password
Be sure to change the csv file location.

![](https://i.imgur.com/4m0y5Eu.png)

### Result
![](https://img.onl/GqjNDt)

### License
MIT

### TODO:
1. Change xpath
2. ~~Ask users Email and password from terminal~~ 