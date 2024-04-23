# Automated Web Crawling and Search System: Enhancing Retrieval Efficiency and Query Understanding

# Abstract

This project develops a comprehensive web crawling and search system that automates the collection of web documents, processes and indexes textual content, and provides an interface for querying and retrieving information. The primary objective was to design a system capable of efficiently crawling websites, indexing retrieved documents using TF-IDF scoring, and facilitating search queries through a simple web interface. Future steps include enhancing query processing with natural language understanding and improving the system's scalability and efficiency.

# Overview

The proposed system comprises three main components: a web crawler built with Scrapy for downloading HTML documents, a text indexer using Scikit-Learn for creating an inverted index, and a Flask-based web application for handling search queries. This approach was influenced by existing literature on information retrieval systems and search engines, focusing on efficiency and scalability.


# Design

# System Capabilities

•	Web Crawler: Dynamically crawls and stores web pages up to a specified depth and page limit.
•	Indexer: Processes text from HTML documents to construct an inverted index based on TF-IDF weights.
•	Query Processor: Accepts and processes user queries to return the most relevant documents.

# Interactions

•	Users interact with the system through a web interface where they can submit queries.
•	The backend processes these queries against the inverted index and returns ranked results.
Integration
•	The system integrates web crawling, text indexing, and query processing in a seamless workflow, facilitating easy transitions from one stage to the next.



# Architecture

# Software Components

•	Scrapy: Handles web crawling.
•	BeautifulSoup & Scikit-Learn: Used for parsing HTML and indexing text.
•	Flask: Provides the web interface and query processing backend.
Interfaces
•	The user interface is web-based, accessible through standard web browsers.
•	Backend processes communicate through internal APIs and shared files (like the inverted index).


# Implementation

•	Python was chosen for its robust libraries and ease of integration between components.


![WhatsApp Image 2024-04-22 at 23 54 40_5fcecf7a](https://github.com/varunkhareedu/IR-Project/assets/70313728/d8adb751-2b80-4c5b-97b9-c49ddf8d5b40)

![WhatsApp Image 2 ](https://github.com/varunkhareedu/IR-Project/assets/70313728/4a1f8f38-a734-454a-a3a8-16f1bc18802e)


# Operation

# Commands

•	Run the crawler with scrapy crawl web_document_spider.
•	Start the Flask app with python app.py.
Inputs
•	The crawler takes a starting URL and limits for depth and pages.
•	The Flask app takes search queries through a web form.



# Installation

•	Requires Python, Scrapy, Flask, BeautifulSoup, Scikit-Learn, and NLTK. Install dependencies via pip install -r requirements.txt.


# Conclusion

The project successfully meets its goal of enabling efficient information retrieval from a corpus of web-crawled documents. It effectively demonstrates basic capabilities but could be improved with advanced natural language processing and better error handling.

![WhatsApp 1](https://github.com/varunkhareedu/IR-Project/assets/70313728/7f729397-9eb0-457e-9a24-f7d7b093241f)



# Data Sources

•	The primary data source is the web, with documents crawled from specified domains.


# Test Cases

•	Test coverage includes crawler boundary conditions, indexer accuracy, and query processor resilience.
•	Utilize frameworks like unittest for Python to implement test cases.


# Source Code

•	Provided in the initial query, documented with inline comments.
•	Dependencies include open-source libraries listed in a requirements file.

