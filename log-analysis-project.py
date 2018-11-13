#!/usr/bin/env python3

import psycopg2
from datetime import datetime


most_popular_three_articles = """SELECT articles.title, COUNT(path)
                                 AS most_viewed FROM log JOIN articles
                                 ON articles.slug
                                 = REPLACE(path, '/article/', '')
                                 WHERE path LIKE '%/article/%'
                                 GROUP BY articles.title
                                 ORDER BY COUNT(path) DESC
                                 LIMIT 3;"""


most_popular_authors = """SELECT DISTINCT authors.name, COUNT(path) AS count
                          FROM log JOIN articles
                          ON articles.slug = REPLACE(path, '/article/', '')
                          JOIN authors ON articles.author = authors.id
                          GROUP BY  authors.name
                          ORDER BY count DESC;"""


requests_lead_to_errors = """SELECT to_char(error_days.error_day, 'FMMonth DD, YYYY'),
           ROUND((error_days.error_count::numeric/
                  all_days.day_requests * 100), 2) AS error_percetage
            FROM (
                SELECT DATE(time) AS day, COUNT(*) AS day_requests
                FROM log
                GROUP BY day
            ) AS all_days,
            (
                SELECT DATE(time) AS error_day, count(*) AS error_count
                FROM log
                WHERE status = '404 NOT FOUND'
                GROUP BY error_day
            ) AS error_days
            WHERE all_days.day = error_days.error_day
            AND error_days.error_count > (all_days.day_requests / 100)
            ORDER BY error_days.error_count DESC;"""


def connect():
    return psycopg2.connect(dbname="news")


def most_popular_articles():
    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(most_popular_three_articles)
            popular_articles = cursor.fetchall()
            print("Most Popular Articles of all time? ")

            for article, views in popular_articles:
                print('\t "{0}" - {1} views'.format(article, views))
            print()


def most_popular_author():
    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(most_popular_authors)
            popular_authors = cursor.fetchall()
            print("Most Popular Authors?")

            for author, views in popular_authors:
                print('\t {0} - {1} views'.format(author, views))
            print()


def lead_to_errors():
    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(requests_lead_to_errors)
            error_rate = cursor.fetchall()
            print("days more than 1% of requests lead to errors?")
            print()

            for i in error_rate:
                date = i[0]
                percent = i[1]
                print("\t {0} - {1}% errors".format(date, percent))
                print()


if __name__ == "__main__":
    print()
    most_popular_articles()
    most_popular_author()
    lead_to_errors()
