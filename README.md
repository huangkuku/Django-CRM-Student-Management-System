# 結合 CRM (顧客管理關係) 和學生管理(Student-Management-System)的 App 

## 顧客管理關係CRM(Customer Relationship Management)
此為簡易的顧客管理關係CRM(Customer Relationship Management)平台，
收集客戶的相關資訊，如姓名、電話、Email，地址、購買量等資訊，
以增進企業與客戶之間的關係，增加企業銷售收入和提高客戶留存

## 學生管理平台頁面
首頁可以看到所有學生姓名、學號、email、國小或國中、年級等，點開右邊check鍵彈出小視窗看到該學生以上基本資訊外還有國英數成績，另有編輯、刪除鈕可以編輯跟刪除
All Student 可以看到所有學生所有資訊，另有編輯、刪除鈕可以編輯跟刪除

### This CRM (Customer Relationship Management) App with Django, Python, Bootstrap, MySQL and Plotly express.

![專案封面圖](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/project%20%E5%B0%81%E9%9D%A2.png)


## 功能
會員註冊登入登出、儀錶板、新增、修改、刪除(CRUD)、點開小視窗
```
帳號： Root
密碼： KL982764s810206
```

- [x] 登入
- [x] 登出
...

## 畫面

> 可提供 1~3 張圖片，讓觀看者透過 README 了解整體畫面

![範例圖片 1](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/view_record%20%E9%A6%96%E9%A0%81.png)
![範例圖片 2](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/student%20%E5%B0%81%E9%9D%A2.png)

## 安裝

> 請務必依據你的專案來調整內容。

以下將會引導你如何安裝此專案到你的電腦上。

python 版本建議為：`3.9` 以上, Docker 版本27.2.0, Docker Compose version v2.29.2-desktop.2

### 取得專案

```
git clone https://github.com/huangkuku/Django-CRM-Student-Management-System.git
```

### 安裝套件

```
py -m venv venv
pip install -r requements.txt
docker-compose build
docker-compose up
```

### 運行專案

```
py manage.py runserver 
```

### 開啟專案

在瀏覽器網址列輸入以下即可看到畫面

```
http://127.0.0.1:8000/
```


## 資料夾說明
- classmate - 學生管理系統
- dcrm - 主程式資料夾
- myweb - 顧客管理系統
- mysql - MySQL 資料庫設定、docker-compose.yml、Dockerfile
  
### classmate(學生管理系統) 與 myweb(顧客管理系統)內資料夾說明
- views - 控制器放置處
- urls - 路由放置處
- models - Schema放置處
- forms - django處理的form表單放置處
- templates
  - .html - html檔案放置處
- static 
  - css - bootstrap.min.css 放置處(只有classmate有)


## 專案技術

* Frontend:
  * Bootstrap5
* Backend:
  * Django 5.1
  * MySQL 
        - mysqlclient 2.2.6
  * Plotly express 5.24
  * Docker & docker-compose

## The app will use MySQL for the database.  

## CRM
### View Records
![View Records](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/view_record%20%E9%A6%96%E9%A0%81.png)

### Register
![Register](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/register%E8%A8%BB%E5%86%8A.png)

### Log In, Log Out
![Log In](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/login%E7%99%BB%E5%85%A5.png)
![Log Out](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/logout%E7%99%BB%E5%87%BA.png)

### Add Records
![ Add Records](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/add_record%20%E6%96%B0%E5%A2%9E.png)
![ Add Records2](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/add_record%20%E6%96%B0%E5%A2%9E2.png)
![ Add Records3](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/add_record%20%E6%96%B0%E5%A2%9E3.png)

### Update Records
![Update Records0](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/update_0.png)
![Update Records1](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/update_1.png)
![Update Records2](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/update_2.png)
![Update Records3](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/update_3.png)

### Delete Records 
![Delete Records](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/delete%20%E5%88%AA%E9%99%A4.png)

### Dachborad
![Dachborad](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/dashboard%20%E5%84%80%E9%8C%B6%E6%9D%BF.png)

## Student Management System
[![demo](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/Django%20CRM%20-%20%E5%AD%B8%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%B5%B1%202024-12-23_1.mp4)

[![demo](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/Django%20CRM%20-%20%E5%AD%B8%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%B5%B1%202024-12-23_2.mp4)

[![demo](https://github.com/huangkuku/Django-CRM-Student-Management-System/blob/main/png/Django%20CRM%20-%20%E5%AD%B8%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%B5%B1%202024-12-23_3.mp4)
## 聯絡作者

你可以透過以下方式與我聯絡

- [Gmail](df467289@gmail.com)

