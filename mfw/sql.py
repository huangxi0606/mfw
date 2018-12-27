#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
from . import settings

MYSQL_HOSTS=settings.MYSQL_HOSTS
MYSQL_USER=settings.MYSQL_USER
MYSQL_PASSWORD=settings.MYSQL_PASSWORD
MYSQL_PORT=settings.MYSQL_PORT
MYSQL_DB=settings.MYSQL_DB
mysql_connect_dict = {
            'host': MYSQL_HOSTS,
            'port': 3306,
            'user': MYSQL_USER,
            'password': MYSQL_PASSWORD,
            'db': MYSQL_DB,
            'charset': 'utf8mb4'
        }
cnx=pymysql.connect(**mysql_connect_dict)
cur = cnx.cursor()
class Sql:
    @classmethod
    def insert_travels(cls,title,img,intro,addr,scan,comment,author,created,url,type,timeone,dayone,people,content,cost):
        sql='INSERT INTO travels(`title`,`img`,`intro`,`addr`,`scan`,`comment`,`author`,`created`,`url`,`type`,`timeone`,`dayone`,`people`,`content`,`cost`)VALUES(%(title)s,%(img)s,%(intro)s,%(addr)s,%(scan)s,%(comment)s,%(author)s,%(created)s,%(url)s,%(type)s,%(timeone)s,%(dayone)s,%(people)s,%(content)s,%(cost)s)'
        # print(sql)
        # print('渺小')
        value ={
            'img':img,
            'intro':intro,
            'title':title,
            'addr':addr,
            'scan': scan,
            'comment': comment,
            'author': author,
            'created': created,
            'url': url,
            'type': type,
            'timeone': timeone,
            'dayone': dayone,
            'people': people,
            'content': content,
            'cost': cost,
        }
        cur.execute(sql,value)
        cnx.commit()

    @classmethod
    def select_travels(cls,title):
        # print('无常')
        sql='SELECT EXISTS(SELECT 1 FROM travels WHERE title =%(title)s)'
        value ={
            'title':title
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]