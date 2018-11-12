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


requests_lead_to_errors = """SELECT COUNT(*),DATE(time),(SELECT COUNT(*)
                             FROM log
                             WHERE status = '404 NOT FOUND')
                             AS TotalErrorCount
                             FROM log
                             WHERE status = '404 NOT FOUND'
                             GROUP BY DATE(time)
                             HAVING COUNT(*) > 130
                             ORDER BY COUNT(*) DESC
                             LIMIT 1;"""


def connect():
    return psycopg2.connect(dbname="news")


def most_popular_articles():
    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(most_popular_three_articles)
            popular_articles = cursor.fetchall()
            print("Most Popular Articles of all time? ")

            for article in popular_articles:
                print('\t {0} views'.format('-'.join(map(str, article))))
            print()


def most_popular_author():
    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(most_popular_authors)
            popular_authors = cursor.fetchall()
            print("Most Popular Authors?")

            for author in popular_authors:
                print('\t {0} views'.format('-'.join(map(str, author))))
            print()


def lead_to_errors():
    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(requests_lead_to_errors)
            error_rate = cursor.fetchall()
            print("days more than 1% of requests lead to errors?")
            print()

            for i in error_rate:
                count = i[0]
                date = datetime.strftime(i[1], '%B %d,%Y')
                total_error = i[2]
                percent = ((count / total_error) * 100)
                print("\t {0} - {1:.2f}% errors".format(date, percent))
                print()


if __name__ == "__main__":
    print()
    most_popular_articles()
    most_popular_author()
    lead_to_errors()
